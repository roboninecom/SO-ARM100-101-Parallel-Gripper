"""Strip xacro from the SO-101 URDF, drop the stock Robo9 clamps, compile to MJCF."""
import pathlib
import re
import xml.etree.ElementTree as ET

import mujoco

W = pathlib.Path(__file__).parent
src = (W / "so_101.urdf.xacro").read_text(encoding="utf-8")

# xacro usage here is only includes + one unused arg -> strip them
src = re.sub(r"<xacro:[^>]*/>\s*", "", src)
src = src.replace(' xmlns:xacro="http://www.ros.org/wiki/xacro"', "")
# meshes live next to this file
src = src.replace("package://so_arm_101_description/meshes/visual/", "arm/")
src = src.replace("package://so_arm_101_description/meshes/collision/", "arm/")
src = re.sub(r'meshdir="[^"]*"', 'meshdir="meshes/arm"', src)

root = ET.fromstring(src)
# drop the stock parallel gripper: it is what we are replacing
for tag, attr in (("link", "name"), ("joint", "name")):
    for el in list(root.findall(tag)):
        if el.get(attr) in ("clamp_1", "clamp_2", "right_clamp", "left_clamp"):
            root.remove(el)

out = W / "so_101_arm.urdf"
ET.ElementTree(root).write(out, encoding="utf-8", xml_declaration=True)
print("wrote", out)

m = mujoco.MjModel.from_xml_path(str(out))
print("compiled OK: nbody=%d njnt=%d ngeom=%d nmesh=%d" % (m.nbody, m.njnt, m.ngeom, m.nmesh))
for i in range(m.nbody):
    print("  body %2d %-12s parent=%-12s pos=%s" % (
        i, mujoco.mj_id2name(m, mujoco.mjtObj.mjOBJ_BODY, i),
        mujoco.mj_id2name(m, mujoco.mjtObj.mjOBJ_BODY, m.body_parentid[i]),
        m.body_pos[i].round(6)))
for i in range(m.njnt):
    print("  joint %-22s axis=%s range=%s" % (
        mujoco.mj_id2name(m, mujoco.mjtObj.mjOBJ_JOINT, i),
        m.jnt_axis[i].round(4), m.jnt_range[i].round(4)))
mujoco.mj_saveLastXML(str(W / "so_101_arm.xml"), m)
print("saved MJCF ->", W / "so_101_arm.xml")
