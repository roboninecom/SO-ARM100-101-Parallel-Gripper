"""Open the MuJoCo viewer. Usage: python view.py [xml]  (default: the full arm)"""
import sys

import mujoco
import mujoco.viewer

xml = sys.argv[1] if len(sys.argv) > 1 else "so101_slide_gripper.xml"
m = mujoco.MjModel.from_xml_path(xml)
d = mujoco.MjData(m)
actuator_names = [
    mujoco.mj_id2name(m, mujoco.mjtObj.mjOBJ_ACTUATOR, i) for i in range(m.nu)
]
print("Loaded %s  |  actuators: %s" % (xml, actuator_names))
print(
    "Drag the 'sg_grip' slider (Control panel) between "
    "0 = open (84 mm) and 0.0355 = closed (13 mm)."
)
mujoco.viewer.launch(m, d)
