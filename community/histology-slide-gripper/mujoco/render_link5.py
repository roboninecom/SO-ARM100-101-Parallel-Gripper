import imageio.v2 as imageio
import mujoco
import numpy as np

XML = """
<mujoco>
  <compiler angle="radian" meshdir="meshes/arm"/>
  <visual><global offwidth="1200" offheight="1000"/></visual>
  <asset>
    <mesh name="link5" file="link5_1.stl" scale="0.001 0.001 0.001"/>
    <mesh name="clamp1" file="clamp_1.stl" scale="0.001 0.001 0.001"/>
    <mesh name="clamp2" file="clamp_2.stl" scale="0.001 0.001 0.001"/>
  </asset>
  <worldbody>
    <light pos="0.3 -0.4 0.8" dir="-0.3 0.4 -0.8" directional="true"/>
    <!-- all three meshes carry the same CAD-frame offset, so this shows link5
         exactly as it sits with the STOCK Robo9 clamps -->
    <geom pos="-0.007062 0.120627 -0.152066" type="mesh" mesh="link5" rgba="0.8 0.8 0.82 1"/>
    <geom pos="-0.007062 0.120627 -0.152066" type="mesh" mesh="clamp1" rgba="0.9 0.4 0.2 1"/>
    <geom pos="-0.007062 0.120627 -0.152066" type="mesh" mesh="clamp2" rgba="0.2 0.5 0.9 1"/>
    <site pos="0 0 0" size="0.004" rgba="1 0 1 1"/>
  </worldbody>
</mujoco>"""
m = mujoco.MjModel.from_xml_string(XML)
d = mujoco.MjData(m)
mujoco.mj_forward(m, d)
frames = []
with mujoco.Renderer(m, 800, 700) as r:
    for az, el in ((135, -20), (215, -15), (90, 0), (0, -80)):
        c = mujoco.MjvCamera()
        c.azimuth = az
        c.elevation = el
        c.distance = 0.30
        c.lookat[:] = [0, -0.06, 0.0]
        r.update_scene(d, c)
        frames.append(r.render())
imageio.imwrite("link5_stock.png", np.hstack(frames))
print("wrote link5_stock.png")
