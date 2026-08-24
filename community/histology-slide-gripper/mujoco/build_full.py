"""Assemble the SO-101 arm + the Microscope Slide Gripper into one MJCF."""
import pathlib
import xml.etree.ElementTree as ET

import mujoco

# --- mount of the gripper on link5 -------------------------------------
# The gripper CAD frame: origin at the drive-pinion axis, -Y = jaw pointing
# direction, +-X = jaw travel, +Z = pinion axis.
# Solved by aligning your CAD against link5_1.stl over the shared guide rods and
# main frame (24 axis-aligned rotations, best fit: +90 deg about X, 2.0 mm median
# residual).  CAD +Y -> link5 +Z, CAD +Z -> link5 -Y.
MOUNT_POS = "-0.0014 -0.0477 -0.0002"
MOUNT_QUAT = "0.70710678 0.70710678 0 0"
# -----------------------------------------------------------------------

W = pathlib.Path(__file__).parent
tree = ET.parse(W / "so_101_arm.xml")
root = tree.getroot()
root.set("model", "so101_slide_gripper")

# the gripper include carries full paths, so flatten meshdir and re-root the arm meshes
comp = root.find("compiler")
comp.set("meshdir", ".")
for mesh in root.find("asset").findall("mesh"):
    mesh.set("file", "meshes/arm/" + mesh.get("file"))


def sub(parent, tag, **kw):
    e = ET.SubElement(parent, tag)
    for k, v in kw.items():
        e.set(k.rstrip("_"), v)
    return e


# options / visual quality
opt = ET.Element("option")
opt.set("timestep", "0.002")
opt.set("integrator", "implicitfast")
root.insert(1, opt)
vis = ET.Element("visual")
sub(vis, "global", offwidth="1600", offheight="1200")
sub(vis, "quality", shadowsize="4096")
root.insert(2, vis)

# gripper mesh assets
root.insert(3, ET.Comment(" gripper geometry, exported from Fusion "))
inc = ET.Element("include")
inc.set("file", "gripper_assets.xml")
root.insert(4, inc)

# scene dressing
asset = root.find("asset")
sub(asset, "texture", name="grid", type="2d", builtin="checker",
    rgb1="0.25 0.27 0.30", rgb2="0.32 0.34 0.38", width="512", height="512")
sub(asset, "material", name="grid", texture="grid", texrepeat="8 8", reflectance="0.1")
sub(asset, "texture", name="sky", type="skybox", builtin="gradient",
    rgb1="0.35 0.42 0.52", rgb2="0.05 0.06 0.08", width="256", height="256")

wb = root.find("worldbody")
wb.insert(0, ET.Element("geom", {"name": "floor", "type": "plane",
                                 "size": "1 1 0.01", "material": "grid"}))
wb.insert(0, ET.Element("light", {"pos": "0.4 -0.5 1.0", "dir": "-0.4 0.5 -1.0",
                                  "directional": "true", "diffuse": "0.7 0.7 0.7"}))
wb.insert(0, ET.Element("light", {"pos": "-0.5 -0.3 0.8", "dir": "0.5 0.3 -0.8",
                                  "diffuse": "0.3 0.3 0.3"}))

# link5_1.stl IS the stock Robo9 gripper (frame + rods + camera), so it is the
# part being replaced: drop its mesh and let your base.stl stand in for it.
link5b = [b for b in wb.iter("body") if b.get("name") == "link5_1"][0]
for g in link5b.findall("geom"):
    link5b.remove(g)
inert = link5b.find("inertial")          # was 0.556 kg incl. the stock gripper
inert.set("mass", "0.08")
inert.set("pos", "0 -0.01 0.005")
inert.set("diaginertia", "6e-05 6e-05 4e-05")
inert.set("quat", "1 0 0 0")

# hang the gripper off link5
link5 = wb.iter("body")
link5 = [b for b in wb.iter("body") if b.get("name") == "link5_1"][0]
mount = ET.SubElement(link5, "body")
mount.set("name", "sg_mount")
mount.set("pos", MOUNT_POS)
mount.set("quat", MOUNT_QUAT)
ET.SubElement(mount, "include").set("file", "gripper_body.xml")

# arm actuators + the gripper's
act = ET.SubElement(root, "actuator")
for j, kp in (("base_link_to_link1", 12), ("link1_to_link2", 18), ("link2_to_link3", 14),
              ("link3_to_link4", 8), ("link4_to_link5", 6)):
    e = ET.SubElement(act, "position")
    e.set("name", j)
    e.set("joint", j)
    e.set("kp", str(kp))
    e.set("kv", str(round(kp / 6, 2)))
    e.set("forcerange", "-1.5 1.5")
ET.SubElement(root, "include").set("file", "gripper_actuation.xml")

# link5's mesh already contains the wrist shell; don't let it fight the gripper frame
con = ET.SubElement(root, "contact")
e = ET.SubElement(con, "exclude")
e.set("body1", "link5_1")
e.set("body2", "slide_gripper_base")
# base_link is merged into worldbody by the URDF importer, and MuJoCo only skips
# parent/child contacts when the parent is not the world body -- so the base mesh and
# link1 mesh interpenetrate at the shoulder and permanently fight the yaw actuator.
e = ET.SubElement(con, "exclude")
e.set("body1", "world")
e.set("body2", "link1_1")

out = W / "so101_slide_gripper.xml"
ET.indent(tree, space="  ")
tree.write(out, encoding="utf-8", xml_declaration=False)
print("wrote", out)


m = mujoco.MjModel.from_xml_path(str(out))
print("compiled OK: nbody=%d njnt=%d nu=%d neq=%d" % (m.nbody, m.njnt, m.nu, m.neq))
