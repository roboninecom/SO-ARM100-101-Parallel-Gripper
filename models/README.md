# 3D Models

This folder contains STL files for the Follower Gripper assembly.

## Complete Assembly (Preview)

| File | Description | Compatible Printers |
|------|-------------|---------------------|
| `Follower_Gripper_180x180_BedSize.STL` | Complete gripper assembly | Printers with 180×180mm+ bed |

### Compatible 3D Printers (180×180mm bed size)

- **Bambu Lab A1 mini** (180×180×180mm)
- **Prusa MINI / MINI+** (180×180×180mm)
- **Creality Ender-2 Pro** (165×165×180mm - partial fit)
- **Anycubic Kobra Neo** (220×220×250mm)
- **Artillery Genius** (220×220×250mm)

*Note: Any printer with bed size ≥180×180mm can print the complete assembly preview.*

## Individual Parts

Located in the `parts/` folder:

| Part Number | File | Qty | Description |
|-------------|------|:---:|-------------|
| RB9.01.060.015 | `Main frame 128mm (follower).STL` | 1 | Main structural frame |
| RB9.01.060.021 | `Clamp.STL` | 2 | Finger clamps |
| RB9.01.060.030 | `Gear rack (short).STL` | 2 | Gear racks for linear motion |
| RB9.01.060.041 | `Gear for gripper.STL` | 1 | Drive gear |
| RB9.01.060.073 | `Camera holder.STL` | 1 | Camera mounting bracket |

## Print Settings

| Parameter | Recommended Value |
|-----------|-------------------|
| Material | PLA / PETG |
| Layer Height | 0.2mm (0.15mm for gears) |
| Infill | 20% (30% for gears) |
| Supports | As needed |
| Walls | 3-4 perimeters |

## Notes

- Print gears with higher infill (30%) for better strength
- Main frame may require supports depending on orientation
- Post-processing: light sanding may be needed for bearing fits
- Individual parts can be printed on any standard FDM printer (bed size ≥120×120mm)
