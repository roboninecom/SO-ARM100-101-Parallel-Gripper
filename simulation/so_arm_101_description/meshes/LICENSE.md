# Licensing of the meshes in this directory

**This directory is mixed.** Not every mesh here is owned by Robonine, so the
licence is assigned per file rather than per directory.

`collision/` contains convex hulls generated from `visual/` by
`../scripts/generate_collision_meshes.py`. Each hull carries the same licence as
the visual mesh it was generated from.

| File (in both `visual/` and `collision/`) | Licence | Copyright |
|---|---|---|
| `clamp_1.stl`, `clamp_2.stl` | CERN-OHL-P-2.0 | Robonine |
| `base_link.stl` | Apache-2.0 | TheRobotStudio |
| `link1_1.stl`, `link2_1.stl`, `link3_1.stl`, `link4_1.stl` | Apache-2.0 | TheRobotStudio |
| `link5_1.stl` | Apache-2.0 | mixed — see below |

## Upstream geometry

`base_link.stl` and `link1_1.stl` … `link4_1.stl` are the SO-ARM101 **arm**,
derived from the upstream [SO-ARM100/101 project by
TheRobotStudio](https://github.com/TheRobotStudio/SO-ARM100) and redistributed
under Apache-2.0. This project did not design that geometry. See the repository
`NOTICE`.

## `link5_1.stl` — fused mesh

`link5_1.stl` is a single mesh that fuses the upstream SO-ARM101 wrist with
Robonine's `RB9.01.062.010 Main frame`. The whole file is distributed under
**Apache-2.0**: Robonine cannot grant CERN-OHL-P-2.0 over geometry it does not
own, and is free to license its own portion under Apache-2.0.

Re-exporting this as two separate meshes would let each part carry its proper
licence. Until then, treat the file as Apache-2.0 in full.

## Robonine geometry

`clamp_1.stl` and `clamp_2.stl` are Robonine's own design — the
`RB9.01.062.021 Clamp` merged with the `RB9.01.062.031 Gear rack`. They are Open
Hardware under CERN-OHL-P-2.0:

```
Copyright (c) 2025 Robonine

This source describes Open Hardware and is licensed under the CERN-OHL-P v2.
You may redistribute and modify this source and make products using it under
the terms of the CERN-OHL-P v2 (https://ohwr.org/cern_ohl_p_v2.txt).

This source is distributed WITHOUT ANY EXPRESS OR IMPLIED WARRANTY, INCLUDING
OF MERCHANTABILITY, SATISFACTORY QUALITY AND FITNESS FOR A PARTICULAR PURPOSE.

SPDX-License-Identifier: CERN-OHL-P-2.0
```

See the repository `LICENSE` for the full licence map.
