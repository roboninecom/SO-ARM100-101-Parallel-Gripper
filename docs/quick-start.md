# Quick Start Guide

Get your Follower Gripper for SO-ARM101 up and running!

[![SO-ARM101 Parallel Gripper](../assets/images/SO%20ARM%20101%20Parallel%20Gripper%20Live.png)](https://youtube.com/shorts/eL2W2aHTV8M)

*Click the image to [watch the gripper in action](https://youtube.com/shorts/eL2W2aHTV8M)!*

## What You'll Need

### Hardware
- [ ] All 3D printed parts (see [3D Models](../models/))
- [ ] Electronic components (see [BOM](bom.md))
- [ ] Mechanical components (bearings, rods, fasteners)
- [ ] Tools: Phillips screwdriver, Hex keys M3 and M4

### Software
- [ ] Python 3.6+ installed
- [ ] STServo SDK downloaded
- [ ] Serial communication interface

---

## Step 1: 3D Print the Parts (2-4 hours)

1. Download STL files from `models/parts/`
2. Print with recommended settings:
   - Layer height: 0.2mm (0.15mm for gears)
   - Infill: 20% (frame/clamps), 30% (gears)
   - Material: PLA or PETG
3. Remove supports and test-fit bearings

**Compatible 3D Printers** (180×180mm+ bed):
- Bambu Lab A1 mini
- Prusa MINI / MINI+
- Anycubic Kobra Neo
- Any printer with bed ≥180×180mm

**Parts to print:**
- 1x Main frame (RB9.01.060.015)
- 2x Clamp (RB9.01.060.021)
- 2x Gear rack (RB9.01.060.030)
- 1x Gear for gripper (RB9.01.060.041)
- 1x Camera holder (RB9.01.060.073)

---

## Step 2: Gather Components (1-2 days shipping)

Order parts from the [Bill of Materials](bom.md):

| Component | Qty | Est. Cost |
|-----------|:---:|-----------|
| Feetech STS3215 servo | 1 | ~$29 |
| Bus Servo Adapter Board | 1 | ~$11 |
| MR106ZZ bearings (6x10x3mm) | 2 | ~$5 |
| LM6UU linear bearings | 4 | ~$9 |
| Steel rods D6x125mm | 2 | ~$8 |
| Steel rods D6x150mm | 2 | ~$9 |
| Threaded rods M3x150mm | 2 | ~$8 |
| Fasteners (M3, M4 screws/nuts) | various | ~$3 |

**Total estimated cost: ~$76** (excluding 3D printing)

---

## Step 3: Assembly (30-45 minutes)

Follow the detailed [Assembly Guide](assembly-guide.md):

1. **Install linear bearings** in clamps (5 min)
2. **Mount gear** to servo with set screws (5 min)
3. **Attach servo** to main frame (5 min)
4. **Install MR106ZZ bearings** on main frame (5 min)
5. **Add rods and clamps** (5 min)
6. **Attach gear racks** to clamps (5 min)
7. **Insert servo cable** (2 min)
8. **Add rigidity screws** M3x50 (3 min)
9. **Attach to robot arm** (optional) (5 min)

---

## Step 4: Software Setup (10 minutes)

1. **Install STServo SDK**
   ```bash
   git clone https://github.com/FEETECH-RC/STServo_SDK_Python.git
   cd STServo_SDK_Python
   cp -r STservo_sdk /path/to/your/project/
   ```

2. **Install Python dependencies**
   ```bash
   pip install pyserial
   ```

3. **Configure connection**
   ```python
   DEVICENAME = 'COM7'  # Windows
   # DEVICENAME = '/dev/ttyUSB0'  # Linux
   STS_ID = 1  # Servo ID (use 6 if connected as gripper on SO-ARM101)
   ```

---

## Step 5: First Test (5 minutes)

1. **Connect hardware**
   - Servo → Bus Servo Adapter
   - Bus Adapter → Computer (USB)
   - Power supply (6-12V, min 3A)

2. **Run basic test**
   ```bash
   cd software/python
   python gripper_control.py
   ```

3. **Try basic commands**
   - Enter `45` to open gripper
   - Enter `-45` to close gripper
   - Enter `0` to center
   - Press Enter to exit

---

## Troubleshooting

### Connection Issues
- ✅ Check COM port in Device Manager (Windows) or `ls /dev/ttyUSB*` (Linux)
- ✅ Verify servo power LED is on
- ✅ Try different baud rates (default: 1000000)
- ✅ Check cable connections

### Movement Issues
- ✅ Verify gear engagement with rack
- ✅ Check for mechanical binding
- ✅ Ensure bearings move freely on rods
- ✅ Monitor servo temperature (max 60°C)

### Software Issues
- ✅ Install STServo SDK correctly
- ✅ Check Python version (3.6+)
- ✅ Verify serial port permissions: `sudo chmod 666 /dev/ttyUSB0` (Linux)

---

## Next Steps

🎉 **Congratulations!** Your gripper is working!

Now you can:
- Mount on SO-ARM100/101 robot arm
- Integrate with your control software
- Add a camera to the camera holder
- Create custom applications

## Need Help?

- 📖 Read the [Specifications](specifications.md)
- 📖 Check the [Assembly Guide](assembly-guide.md)
- 🐛 Report issues on GitHub

---

**Welcome to the parallel gripper community!** 🤖
