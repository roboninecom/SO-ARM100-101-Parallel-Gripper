# SO-ARM100/101 Parallel Gripper

<div align="center">

[![SO-ARM101 Parallel Gripper](assets/images/SO%20ARM%20101%20Parallel%20Gripper%20Live.png)](https://youtube.com/shorts/eL2W2aHTV8M)

**🎥 [Watch the gripper in action!](https://youtube.com/shorts/eL2W2aHTV8M)**

A lightweight 3D-printed parallel gripper designed by **[Robonine](https://robonine.com)** for the open-source SO-ARM100/101 robotic platform.

[![License: GPL-3.0](https://img.shields.io/badge/License-GPL%203.0-blue.svg)](LICENSE)
[![Cost: ~$76](https://img.shields.io/badge/Cost-~%2476-green.svg)](docs/bom-amazon.md)
[![Assembly: 30min](https://img.shields.io/badge/Assembly-30%20min-orange.svg)](docs/assembly-guide.md)

---

**Questions? We're here to help!**  
📩 Email: [hello@robonine.com](mailto:hello@robonine.com)

</div>

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| 🎯 **500N Gripping Force** | Powerful parallel jaw mechanism |
| ⚡ **60 mm/s Speed** | Fast gripper operation |
| 📏 **100.5mm Full Stroke** | Wide opening for various objects |
| 🎯 **±0.05mm Repeatability** | High precision positioning |
| 📷 **Camera Compatible** | Supports RealSense, Orbbec, USB cameras |
| 🖨️ **3D Printable** | All parts print on standard FDM printers |
| 💰 **~$76 Total Cost** | Affordable open-source solution |
| ⚙️ **Easy Assembly** | 30-45 minutes with basic tools |

---

## 📸 Gallery

<div align="center">

### Gripper on SO-ARM100

![Gripper mounted on SO-ARM100](assets/images/specification/07-gripper-on-so-arm100.jpg)

*Follower gripper integrated with SO-ARM100 robot arm*

### Dimensions

| Closed | Open |
|--------|------|
| ![Closed gripper](assets/images/specification/01-closed-gripper-dimensions.jpg) | ![Open gripper](assets/images/specification/02-open-gripper-dimensions.jpg) |
| Height: 108.4mm, Length: 123.5mm | Full stroke: 100.5mm |

</div>

---

## 📋 Specifications

### Performance

| Parameter | Value |
|-----------|-------|
| Maximum gripping force | **500 N** |
| Maximum gripping speed | **60 mm/s** |
| Full stroke | **100.5 mm** |
| Repeatability | **±0.05 mm** |
| Assembly mass (PLA, 30% infill) | **200 g** |
| DOF | **1** |

### Dimensions

| Dimension | Value |
|-----------|-------|
| Length (closed) | 123.5 mm |
| Height | 108.4 mm |
| Frame width | 102 mm |
| Jaw height | 21.4 mm |
| Jaw thickness | 8.5 mm |

### Servo Motor (Feetech STS3215)

| Parameter | Value |
|-----------|-------|
| Operating Voltage | 4-14V |
| Stall torque | 30 kg·cm |
| Speed (no load) | 45 RPM |
| Encoder | Absolute magnetic 12-bit |
| Protocol | RS485/TTL up to 1 Mbps |
| Operating temperature | -20°C ~ 60°C |

---

## 📷 Camera Compatibility

The gripper supports multiple cameras via interchangeable camera holder:

| Camera | Type | Use Case |
|--------|------|----------|
| IMX335 5MP USB | RGB | Basic vision tasks |
| GC2093 2MP USB | RGB | Budget option |
| Orbbec Gemini 2 | RGB-D | 3D perception |
| RealSense D405 | RGB-D | Close-range depth |
| RealSense D435/D435i | RGB-D | General purpose |
| RealSense D455 | RGB-D | Long-range depth |

<div align="center">

| IMX335 | Orbbec Gemini 2 | RealSense D405 |
|--------|-----------------|----------------|
| ![IMX335](assets/images/specification/04-camera-imx335-5mp.jpg) | ![Orbbec](assets/images/specification/05-camera-orbbec-gemini2.jpg) | ![RealSense](assets/images/specification/06-camera-realsense-d405.jpg) |

</div>

---

## 💰 Bill of Materials

**Total Cost: ~$76** ([Full BOM with Amazon links](docs/bom-amazon.md))

| Category | Components | Est. Cost |
|----------|------------|-----------|
| Electronics | Feetech STS3215 servo + Bus Adapter | ~$40 |
| Bearings | MR106ZZ (2) + LM6UU (4) | ~$6 |
| Rods | D6×125mm (2) + D6×150mm (2) + M3×150mm (2) | ~$10 |
| 3D Printing | 5 parts (~200-300g PLA) | ~$17 |
| Fasteners | M3/M4 screws, nuts, set screws | ~$3 |

---

## 🚀 Quick Start

### 1. Print the Parts (2-4 hours)

Download STL files from [`models/parts/`](models/):

| Part | Qty | Settings |
|------|:---:|----------|
| Main frame (RB9.01.060.015) | 1 | 20% infill |
| Clamp (RB9.01.060.021) | 2 | 20% infill |
| Gear rack (RB9.01.060.030) | 2 | 30% infill |
| Gear (RB9.01.060.041) | 1 | 30% infill |
| Camera holder (RB9.01.060.073) | 1 | 20% infill |

### 2. Order Components (1-2 days)

See [Bill of Materials](docs/bom-amazon.md) for direct Amazon links.

### 3. Assemble (30-45 minutes)

Follow the [Assembly Guide](docs/assembly-guide.md) with step-by-step images:

1. Install linear bearings in clamps
2. Mount gear to servo
3. Attach servo to main frame
4. Install MR106ZZ bearings
5. Add rods and clamps
6. Attach gear racks
7. Insert servo cable
8. Add rigidity screws
9. Mount to robot arm (optional)

### 4. Software Setup

```bash
# Install STServo SDK
git clone https://github.com/FEETECH-RC/STServo_SDK_Python.git

# Install dependencies
pip install pyserial

# Run gripper control
python software/python/gripper_control.py
```

---

## 📁 Repository Structure

```
├── assets/
│   └── images/
│       ├── assembly/          # Assembly step images
│       └── specification/     # Technical drawings
├── docs/
│   ├── assembly-guide.md      # Step-by-step assembly
│   ├── bom-amazon.md          # Bill of materials with links
│   ├── quick-start.md         # Getting started guide
│   └── specifications.md      # Technical specifications
├── models/
│   ├── parts/                 # Individual STL files
│   └── Follower gripper.STL   # Complete assembly preview
├── software/
│   └── python/                # Control software
└── examples/                  # Usage examples
```

---

## 📖 Documentation

| Document | Description |
|----------|-------------|
| [Quick Start Guide](docs/quick-start.md) | Get running in 30 minutes |
| [Assembly Guide](docs/assembly-guide.md) | Step-by-step with images |
| [Bill of Materials](docs/bom-amazon.md) | Parts list with Amazon links |
| [Specifications](docs/specifications.md) | Technical details |
| [3D Models](models/README.md) | Print settings and files |

---

## 🔧 Hardware Requirements

### Electronics
- 1× Feetech STS3215 Servo Motor
- 1× Bus Servo Adapter Board (Waveshare)

### Mechanical
- 2× MR106ZZ Bearings (6×10×3 mm)
- 4× LM6UU Linear Bearings (6×12×19 mm)
- 2× Steel Rods D6×125 mm
- 2× Steel Rods D6×150 mm
- 2× Threaded Rods M3×150 mm

### Fasteners
- 8× M3×8 DIN 7991 screws
- 4× M3×20 DIN 7991 screws
- 4× M3×50 DIN 912 screws
- 2× M4×6 DIN 7991 screws
- 4× M3 DIN 934 nuts
- 4× M3×4 DIN 913 set screws

### Tools Required
- Phillips head screwdriver
- Hex keys M3 and M4

---

## 🤝 Contributing

We welcome contributions! Please feel free to:
- 🐛 Report bugs and issues
- 💡 Suggest new features
- 🔧 Submit pull requests
- 📖 Improve documentation

---

## 📄 License

This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details.

---

## 🔗 Links

- [Feetech STS3215 Servo](https://www.feetechrc.com/525603.html)
- [Waveshare Bus Servo Adapter](https://www.waveshare.com/bus-servo-adapter-a.htm)
- [STServo Python SDK](https://github.com/FEETECH-RC/STServo_SDK_Python)

---

<div align="center">

**Built for the robotics community by [Robonine](https://robonine.com)** 🤖

**Questions? We're here to help!**  
📩 Email: [hello@robonine.com](mailto:hello@robonine.com)

</div>
