"""Close the jaws on a test object, lift it, and render the sequence."""
import imageio.v2 as imageio
import mujoco
import numpy as np

m = mujoco.MjModel.from_xml_path("scene_gripper.xml")
d = mujoco.MjData(m)
GRIP, LIFT = m.actuator("sg_grip").id, m.actuator("lift").id
jr = m.joint("sg_jaw_right_joint").qposadr[0]
obj = m.body("slide").id

cam = mujoco.MjvCamera()
cam.lookat[:] = [0, -0.028, 0.06]
cam.distance = 0.40
cam.azimuth = 140
cam.elevation = -15
opt = mujoco.MjvOption()
opt.geomgroup[3] = 0
frames = []


def shot(r, label):
    r.update_scene(d, cam, opt)
    frames.append(r.render())
    print("%-9s aperture=%5.1f mm   object z=%.4f   ncon=%d" %
          (label, 84 - 2000 * d.qpos[jr], d.xpos[obj][2], d.ncon))


def run(n, ctrl, ramp=False):
    start = {a: d.ctrl[a] for a in ctrl}
    for k in range(n):
        f = min(1.0, (k + 1) / n) if ramp else 1.0
        for a, v in ctrl.items():
            d.ctrl[a] = start[a] + (v - start[a]) * f
        mujoco.mj_step(m, d)


with mujoco.Renderer(m, 900, 1100) as r:
    run(400, {GRIP: 0.0, LIFT: 0.0})
    shot(r, "open")
    run(1200, {GRIP: 0.0355, LIFT: 0.0}, ramp=True)
    shot(r, "clamped")   # over-close -> squeeze
    run(1500, {GRIP: 0.0355, LIFT: 0.15}, ramp=True)
    run(800, {GRIP: 0.0355, LIFT: 0.15})
    shot(r, "lifted")

z = d.xpos[obj][2]
print("\ngrip force at the pads: %.2f N" % abs(d.actuator_force[GRIP]))
print("RESULT: object lifted to z=%.4f -> %s" % (z, "HELD" if z > 0.08 else "DROPPED"))
imageio.imwrite("grasp_check.png", np.hstack(frames))
print("wrote grasp_check.png")
