# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

An open-source hardware project: a 3D-printed parallel gripper for the SO-ARM100/101 robot arm (by Robonine). Multi-licensed: CERN-OHL-P-2.0 for hardware/CAD, Apache-2.0 for software, CC BY 4.0 for docs — the map is in `LICENSING.md`, the machine-readable version in `REUSE.toml`, third-party attribution in `NOTICE`. New files must be covered by `REUSE.toml`; `reuse lint` runs in pre-commit. Most of the repo is CAD models (`models/`), documentation (`docs/`), and images (`assets/`). Code lives in two places:

- `software/python/gripper_control.py` — standalone servo control script for the Feetech STS3215 (depends on the STServo SDK, which is cloned manually — see `software/python/requirements.txt`; it is not on PyPI). `examples/basic_usage.py` imports from it via a `sys.path` hack.
- `simulation/so_arm_101_description/` — a ROS2 (Humble) description package that simulates the arm+gripper in 5 physics engines. This is where all tests and most CI live.

## Commands

```bash
# Lint (what CI runs; hooks exclude STL/STEP files)
pre-commit run --all-files

# Offline tests (65 pytest tests; deps: pytest trimesh numpy mujoco pyyaml)
cd simulation/so_arm_101_description
python -m pytest test/ -v

# Single test file / single test
python -m pytest test/test_urdf_structure.py -v
python -m pytest test/test_config.py -k <name> -v

# Validate xacro/URDF XML without ROS2
python simulation/so_arm_101_description/scripts/validate_xml.py simulation/so_arm_101_description/urdf/*.xacro

# Docker (from simulation/so_arm_101_description/; no ROS2 install needed)
docker compose run test          # run pytest suite
docker compose run validate      # xacro + check_urdf for all 5 backends
docker compose run check-launch  # verify launch files parse
docker compose run gazebo        # or: mujoco, webots, rviz (need X11)
```

CI (`.github/workflows/ci.yaml`) runs: pre-commit, XML/YAML validation, `xacro ... sim_backend:=<backend> | check_urdf` for all 5 backends inside a `ros:humble` container, and the pytest suite. A URDF change must remain valid for **all** backends, not just the one you're targeting.

## Simulation architecture

One parameterized robot description drives every simulator:

- `urdf/so_101.urdf.xacro` is the single source of truth. The xacro arg `sim_backend:=gazebo|mujoco|webots|coppeliasim|isaac` selects the `ros2_control` plugin (via `urdf/so_101.ros2_control.xacro`) at expansion time.
- `config/controllers.yaml` defines identical joints/controllers for all backends; `launch/sim.launch.py` with `sim:=<backend>` is the single entry point.
- Robot: 5-DOF arm + gripper with 2 prismatic clamp joints, where the left clamp mirrors the right via `<mimic>`.
- Meshes are split: `meshes/visual/` (high-poly) vs `meshes/collision/` (convex hulls, regenerated with `scripts/generate_collision_meshes.py`).

A change to joints, links, or controller names typically needs coordinated edits across the xacro files, `controllers.yaml`, and the tests in `test/`.

## CAD models and part numbering

Parts in `models/parts/` use Robonine part numbers (e.g. `RB9.01.062.010 Main frame.STL`). These numbers are referenced throughout `README.md` (print table), `docs/bom.md`, and `docs/assembly-guide.md` — adding or renaming a part means updating those docs too. STLs are binary; variants encode fit tolerances in the filename (e.g. `RB9.01.062.021 (D6.1) Clamp.STL` for different rod diameters). Pre-commit hooks (whitespace, EOF, line endings) deliberately exclude `.stl/.STL/.STEP` files, and files over 1 MB are rejected by `check-added-large-files`.

## Conventions

- Python: flake8 with `--max-line-length=100`, isort with black profile (enforced by pre-commit; `software/` and `examples/` are excluded from flake8).
- Docs are duplicated by design (README summarizes bom.md, specifications.md, assembly-guide.md) — keep them consistent when changing specs, parts, or prices.
- Do not add a `Co-Authored-By: Claude` line to commits.
