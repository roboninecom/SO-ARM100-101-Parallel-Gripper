import sys, numpy as np, mujoco, imageio.v2 as imageio
xml = sys.argv[1] if len(sys.argv)>1 else "so101_slide_gripper.xml"
out = sys.argv[2] if len(sys.argv)>2 else "arm_check.png"
m = mujoco.MjModel.from_xml_path(xml); d = mujoco.MjData(m)
mujoco.mj_forward(m, d)
opt = mujoco.MjvOption(); opt.geomgroup[3] = 0
views = [(135,-20,0.55,[0,-0.10,0.18]), (215,-15,0.45,[0,-0.14,0.16]), (90,-8,0.30,[0,-0.20,0.13])]
frames=[]
with mujoco.Renderer(m, 950, 800) as r:
    for az,el,dist,la in views:
        c=mujoco.MjvCamera(); c.azimuth=az; c.elevation=el; c.distance=dist; c.lookat[:]=la
        r.update_scene(d,c,opt); frames.append(r.render())
imageio.imwrite(out, np.hstack(frames)); print("wrote",out)
b=m.body("slide_gripper_base").id
print("gripper base world pos:", d.xpos[b].round(4))
print("tcp site world pos:", d.site("sg_tcp").xpos.round(4))
