# Licensing of the meshes in this directory

**This directory is mixed.**

`base.stl`, `jaw_left.stl`, `jaw_right.stl`, `pinion.stl` are the community
slide-gripper geometry, exported from Fusion by the variant's author:

```
Copyright (c) 2025 Michael Viacheslavov (@histochemichael)
SPDX-License-Identifier: CERN-OHL-P-2.0
```

`arm/*.stl` are **not** original to this directory. They are byte-identical
copies of `simulation/so_arm_101_description/meshes/visual/*.stl` and inherit
their licensing from there — which is Apache-2.0, because that geometry is
derived from the upstream SO-ARM101 design by TheRobotStudio.

See `simulation/so_arm_101_description/meshes/LICENSE.md` for the per-file
breakdown, the repository `LICENSE` for the licence map, and `NOTICE` for
attribution.
