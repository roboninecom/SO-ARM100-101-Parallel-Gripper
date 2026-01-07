# SO ARM 100/101 Parallel Gripper

## Overview

Lightweight 3D-printed end-effector designed by **Robonine Team** for the open-source teleoperating robotic platform SO ARM 100/101. The mechanism provides reliable parallel jaw motion and sufficient gripping force for a broad range of educational and experimental applications.

![Follower gripper mounted on SO-ARM100](../assets/images/specification/07-gripper-on-so-arm100.jpg)

*Follower gripper mounted on SO-ARM100 robot arm*

## Key Features

- Open-source design
- BOM cost for one gripper: ~$76
- Can be printed on consumer-grade FDM 3D printers
- Compatible with popular video cameras:
  - Orbbec Gemini 2
  - RealSense D405, D435/D435i, D455
  - GC2093 2MP USB Camera Module
  - IMX335 5MP USB Camera

---

## Dimensions

### Closed Gripper

![Closed gripper dimensions](../assets/images/specification/01-closed-gripper-dimensions.jpg)

*Closed gripper showing height (108.4 mm) and length (123.5 mm)*

### Open Gripper

![Open gripper dimensions](../assets/images/specification/02-open-gripper-dimensions.jpg)

*Open gripper showing full stroke width (100.5 mm), frame width (102 mm), and jaw dimensions*

| Dimension | Value |
|-----------|-------|
| Length (closed) | 123.5 mm |
| Height | 108.4 mm |
| Frame width | 102 mm |
| Full stroke | 100.5 mm |
| Jaw height | 21.4 mm |
| Jaw thickness | 8.5 mm |

---

## Mounting Interface

![Mounting interface dimensions](../assets/images/specification/03-mounting-interface.jpg)

*Mounting flange with hole pattern for robot arm attachment*

| Feature | Dimension |
|---------|-----------|
| Mounting flange diameter | Ø20 mm |
| Center bore | Ø7 mm |
| Mounting holes | 4x Ø3.2 mm |

---

## Performance Specifications

| Parameter | Follower Gripper |
|-----------|------------------|
| Assembly mass (PLA, 30% infill) | 200 g (excluding camera) |
| Maximum gripping force | 500 N |
| Maximum gripping speed | 60 mm/s |
| Full stroke | 100.5 mm |
| Repeatability | ±0.05 mm |
| DOF | 1 |

---

## Technical Specifications

### Materials & Construction

| Component | Specification |
|-----------|---------------|
| Primary material | PETG / PLA |
| Transmission | Rack and pinion |
| Guides | Round stainless steel rods (Ø6 mm) |
| Driver | Feetech servo actuator STS3215 |

### Servo Motor (Feetech STS3215)

| Parameter | Value |
|-----------|-------|
| Operating Voltage Range | 4-14V |
| Speed (no load) | 45 RPM |
| Running current (no load) | 180 mA |
| Stall torque (at locked) | 30 kg·cm |
| Stall current (at locked) | 2.7 A |
| Idle current (at stopped) | 30 mA |
| Rated torque | 10 kg·cm |
| Rated current | 900 mA |
| Terminal resistance | 1 Ω |
| Operating temperature | -20°C ~ 60°C |
| Encoder type | Absolute magnetic 12-bit |
| Control protocol | RS485/TTL up to 1 Mbps |
| Electronic protection | Against high voltage, current, load, and temperature |

---

## Camera Compatibility

The Follower gripper is compatible with various cameras via interchangeable camera holder.

### IMX335 5MP USB Camera

![Gripper with IMX335 5MP USB Camera](../assets/images/specification/04-camera-imx335-5mp.jpg)

*Compact USB camera module for basic vision tasks*

### Orbbec Gemini 2

![Gripper with Orbbec Gemini 2 Camera](../assets/images/specification/05-camera-orbbec-gemini2.jpg)

*Depth camera for 3D perception and object detection*

### Intel RealSense D405

![Gripper with RealSense D405 Camera](../assets/images/specification/06-camera-realsense-d405.jpg)

*High-precision depth camera for close-range applications*

### Supported Cameras

| Camera | Type | Notes |
|--------|------|-------|
| IMX335 5MP USB | RGB | Compact, low-cost |
| GC2093 2MP USB | RGB | Budget option |
| Orbbec Gemini 2 | RGB-D | Depth sensing |
| RealSense D405 | RGB-D | Close-range depth |
| RealSense D435/D435i | RGB-D | General purpose |
| RealSense D455 | RGB-D | Long-range depth |

---

## Supplied Resources

- Complete set of STL files for 3D printing
- Assembly guide
- Drawings with mounting dimensions
- URDF file for robotic simulators

---

## Integration

The gripper can be independently integrated into numerous robotic systems thanks to its convenient and simple installation via the standard mounting flange.

### Mounting Requirements

- 4x M3 screws for flange attachment
- Compatible with SO-ARM100/101 robot arm
- Custom adapter plates available for other robot arms

### Communication

- Serial connection via TTL or RS485
- Baud rate: Up to 1 Mbps
- Protocol: Feetech STS protocol

---

*Specifications subject to change based on actual implementation and testing*
