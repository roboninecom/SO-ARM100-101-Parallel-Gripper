# Relicensing record

This file records how and why this project moved off GPL-3.0, and the agreement
of its contributors. It exists so the licence history is auditable without
digging through git.

**Status: IN PROGRESS.** This change must not be merged until every ack below is
recorded.

## What changed

| Material | Before | After |
|---|---|---|
| Hardware / CAD | GPL-3.0-only | CERN-OHL-P-2.0 |
| Software | GPL-3.0-only | Apache-2.0 |
| Documentation and images | GPL-3.0-only | CC BY 4.0 |

Copyright holder: **Robonine**. See `LICENSING.md` for the file-by-file map,
`REUSE.toml` for the machine-readable version, and `NOTICE` for third-party
attribution.

## Why

GPL-3.0 is written for software. Its definitions — "source code", "object
code", "Corresponding Source" — do not map cleanly onto a physical object, so
for the CAD portion of this project it was never clear what actually triggered
the licence's obligations. CERN-OHL-P-2.0 is written for hardware and says
plainly what a Product, Covered Source and Available Component are.

The permissive choice is deliberate. It trades away protection against closed
forks of the gripper in exchange for zero friction for integrators, and for
compatibility with the upstream SO-ARM100/101 project and the wider
LeRobot/ROS ecosystem, which are Apache-2.0 throughout.

## Licence history

| Commit | Date | What |
|---|---|---|
| `00fae7b` | 2025-06-27 | Repository created. `LICENSE` was **MIT** (21 lines). |
| `64d3f01` | 2025-07-01 | `LICENSE` replaced with GPL-3.0 (674 lines). |
| `d37855a` | 2025-07-06 | `README.md` updated from MIT to GPL-3.0. |
| this change | — | Three-way split described above. |

`CONTRIBUTING.md` and `software/python/gripper_control.py` were **never**
updated in 2025 and continued to state MIT. That was an oversight, not
deliberate dual-licensing.

The consequence matters: every external contributor joined *after* the GPL flip,
in a repository whose `CONTRIBUTING.md` still told them *"By contributing, you
agree that your contributions will be licensed under the MIT License."* The
licence they were actually offered was more permissive than GPL-3.0. This change
brings the repository into line with what contributors were told, not against
it. We are nonetheless asking each of them explicitly rather than relying on
that.

## Contributor agreement

| Contributor | Commits | Scope | Ack |
|---|---|---|---|
| Robonine (Nikita Bragin — also `brnikita`, `branikita`) | 76 | Owner | n/a |
| AlanWorkaholic (Alan Subin) | 44 | `models/`, `models/parts/`, `assets/images/`, `docs/` | Work made under contract with IP assignment to Robonine; ack requested as a courtesy |
| histochemichael (Michael Viacheslavov) | 3 + files uploaded on his behalf | `community/histology-slide-gripper/` | _pending_ |
| Vladimir Osipov | 1 | `README.md` dead-link fix | _pending_ |
| Syed Azhar Hussain Quadri | 1 | `software/python/gripper_control.py` | _pending_ |

Relicensing issue: _to be filled in_

### Authorship notes

- Commits authored as `Codex <codex@openai.com>` were made by Nikita Bragin on
  behalf of Robonine. They are not third-party contributions.
- The community variant's CAD and images
  (`community/histology-slide-gripper/cad/*`, `assets/*`) were **committed by
  Robonine on Michael Viacheslavov's behalf** — commits `537f347` and `b4698e7`
  are authored as `Codex`. Authorship of those files belongs to Michael; git
  metadata does not reflect that, which is why it is written down here.

## Decisions on the record

**`link5_1.stl` is a fused mesh.** It combines the upstream SO-ARM101 wrist with
Robonine's `RB9.01.062.010 Main frame` in a single body. The parts are not
separable within the file, so the whole file is distributed under Apache-2.0:
Robonine cannot grant CERN-OHL-P-2.0 over geometry it does not own, and is free
to license its own portion under Apache-2.0. Re-exporting it as two meshes would
let each part carry its proper licence; that is left as future work.

**Notices for binary files.** CERN-OHL-P-2.0 expects licence notices to be
retained in the Source. Binary STL and STEP files cannot carry them, and
`.pre-commit-config.yaml` deliberately excludes those formats from text hooks.
`REUSE.toml` is how this project discharges that obligation: it assigns
copyright and licence to every file by path, and `reuse lint` enforces that
nothing is left uncovered.

Directory-level notices were deliberately kept to a minimum — only where they
carry information the root map does not. Two survive:
`simulation/so_arm_101_description/meshes/LICENSE.md`, because that directory
mixes Robonine and upstream geometry and someone copying a mesh out needs to see
that; and `simulation/so_arm_101_description/LICENSE.md`, because that ROS
package is distributed standalone and has to be self-describing.

**Licence texts exist in two places.** `LICENSES/` is where the REUSE
Specification requires them; `HARDWARE-LICENSE.txt`, `SOFTWARE-LICENSE.txt` and
`DOCS-LICENSE.txt` at the root are what GitHub's licence detection reads, so the
repository shows all three licences rather than none.

**`software/FD.exe` was removed.** It is Feetech's proprietary "FT SCServo Debug"
tool, committed in `7783073` with no licence grant, and was covered by the
project's blanket GPL-3.0 claim — which was incorrect. `docs/assembly-guide.md`
now points to Feetech's own download and to an open-source alternative.

**Git history was not rewritten.** `FD.exe` remains in history and in the source
archives of releases `v0.1.0` through `v0.3.1`. Rewriting would invalidate every
clone, fork and commit SHA referenced from open upstream pull requests, which is
not worth it for a tool Feetech distributes free of charge.

**`ament_copyright` was dropped** from `package.xml`. It was declared but never
wired up or run. It checks for licence headers inside source files, which
conflicts with this project's approach of declaring licences in `REUSE.toml` —
forced on us by the fact that most files here are binaries. `reuse lint` covers
every file in the repository, not just the dozen Python files inside the ROS
package.

## Releases

This does not retroactively change releases `v0.1.0` through `v0.3.1`, which
remain available under GPL-3.0-only.

---

Prepared by the project maintainers. This is a record of decisions, not legal
advice.
