#!/usr/bin/env python3
"""
Parallel Gripper Control Software
=================================

Professional control software for the open-source parallel gripper using
Feetech STS3215 servo motors. Provides real-time control, monitoring, and
feedback for robotics applications.

Features:
- Precise position control with degree-based input
- Real-time monitoring (position, current, voltage, temperature, load)
- Cross-platform compatibility (Windows, Linux, macOS)
- Interactive control interface
- Comprehensive error handling

Requirements:
- STServo SDK (https://github.com/FEETECH-RC/STServo_SDK_Python)
- Python 3.6+
- Serial communication interface

Author: Robonine (https://robonine.com)
License: Apache-2.0

Portions of this file were contributed while it was offered under the MIT
Licence; those contributions are relicensed here under Apache-2.0 with the
contributor's agreement. See RELICENSING.md.
"""

# SPDX-FileCopyrightText: Copyright (c) 2025 Robonine
# SPDX-License-Identifier: Apache-2.0

import logging
import os
import sys
import time
from pathlib import Path
from typing import Optional, Tuple

import serial.tools.list_ports

# Cross-platform keyboard input handling
if os.name == 'nt':
    import msvcrt
    def getch():
        """Get single character input (Windows)"""
        return msvcrt.getch().decode()
else:
    import termios
    import tty
    def getch():
        """Get single character input (Unix/Linux/macOS)"""
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            return sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

# Graceful SDK path handling using pathlib
sdk_path = Path(__file__).resolve().parent.parent / "STservo_sdk"
sys.path.append(str(sdk_path))

try:
    from STservo_sdk import *
except ImportError:
    print("Error: STServo SDK not found!")
    print("Please install STServo SDK from: https://github.com/FEETECH-RC/STServo_SDK_Python")
    print("Copy the STservo_sdk folder to your project directory or Python path.")
    sys.exit(1)

# Dynamic COM port selection
print("\n🔌 Available COM ports:")
ports = list(serial.tools.list_ports.comports())
if not ports:
    print("❌ No COM ports found. Please connect your device and try again.")
    sys.exit(1)
for idx, port in enumerate(ports):
    print(f"  [{idx}] {port.device}")

choice = input("Select port number (default 0): ").strip()
SELECTED_PORT = ports[int(choice)].device if choice.isdigit() and int(choice) < len(ports) else ports[0].device

# Configuration Constants
class GripperConfig:
    """Configuration parameters for the parallel gripper"""

    # Servo Configuration
    STS_ID = 1                  # Servo ID (can be changed if multiple servos)
    BAUDRATE = 1000000         # Communication baud rate (1 Mbps)
    DEVICENAME = SELECTED_PORT  # Dynamic port from user selection

    # Motion Parameters
    MAX_DEGREE = 360           # Maximum rotation (degrees)
    MAX_POSITION = 4095        # Maximum position value (12-bit resolution)
    DEFAULT_SPEED = 4800       # Default movement speed
    DEFAULT_ACCELERATION = 5   # Default acceleration

    # Monitoring Parameters
    LSB_TO_mA = 2700 / 2047   # Current conversion factor (~1.32 mA per LSB)
    VOLTAGE_SCALE = 0.1       # Voltage scale factor (0.1V per LSB)
    LOAD_SCALE = 100 / 2047   # Load percentage scale factor

    # Safety Limits
    MAX_TEMPERATURE = 70      # Maximum safe temperature (°C)
    MAX_CURRENT = 2000        # Maximum safe current (mA)

    # Update Intervals
    MONITOR_INTERVAL = 0.05   # Monitoring update interval (seconds)

class ParallelGripper:
    """
    Main class for controlling the parallel gripper

    Provides high-level interface for gripper control, monitoring, and safety.
    """

    def __init__(self, config: GripperConfig = None):
        """
        Initialize the gripper controller

        Args:
            config: Configuration object (uses default if None)
        """
        self.config = config or GripperConfig()
        self.port_handler = None
        self.packet_handler = None
        self.is_connected = False

        # Setup logging
        logging.basicConfig(level=logging.INFO,
                          format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)

    def connect(self) -> bool:
        """
        Establish connection to the servo

        Returns:
            bool: True if connection successful, False otherwise
        """
        try:
            self.port_handler = PortHandler(self.config.DEVICENAME)
            self.packet_handler = sts(self.port_handler)

            if not self.port_handler.openPort():
                self.logger.error(f"Failed to open port {self.config.DEVICENAME}")
                return False

            if not self.port_handler.setBaudRate(self.config.BAUDRATE):
                self.logger.error(f"Failed to set baud rate to {self.config.BAUDRATE}")
                return False

            # Set servo to position control mode
            self.packet_handler.write1ByteTxRx(self.config.STS_ID, 33, 0)

            self.is_connected = True
            self.logger.info(f"Connected to servo ID {self.config.STS_ID} on {self.config.DEVICENAME}")
            return True

        except Exception as e:
            self.logger.error(f"Connection failed: {e}")
            return False

    def disconnect(self):
        """Close the connection to the servo"""
        if self.port_handler and self.is_connected:
            self.port_handler.closePort()
            self.is_connected = False
            self.logger.info("Disconnected from servo")

    def degrees_to_position(self, degrees: float) -> int:
        """
        Convert degrees to servo position value

        Args:
            degrees: Angle in degrees (can be negative)

        Returns:
            int: Servo position value (0-4095)
        """
        degrees = degrees % self.config.MAX_DEGREE
        return int((degrees / self.config.MAX_DEGREE) * self.config.MAX_POSITION)

    def position_to_degrees(self, position: int) -> float:
        """
        Convert servo position value to degrees

        Args:
            position: Servo position value (0-4095)

        Returns:
            float: Angle in degrees
        """
        return (position / self.config.MAX_POSITION) * self.config.MAX_DEGREE

    def move_to_angle(self, angle: float, speed: int = None, acceleration: int = None) -> bool:
        """
        Move gripper to specified angle

        Args:
            angle: Target angle in degrees
            speed: Movement speed (uses default if None)
            acceleration: Movement acceleration (uses default if None)

        Returns:
            bool: True if command sent successfully, False otherwise
        """
        if not self.is_connected:
            self.logger.error("Not connected to servo")
            return False

        speed = speed or self.config.DEFAULT_SPEED
        acceleration = acceleration or self.config.DEFAULT_ACCELERATION

        goal_position = self.degrees_to_position(angle)

        try:
            result, error = self.packet_handler.WritePosEx(
                self.config.STS_ID, goal_position, speed, acceleration
            )

            if result != COMM_SUCCESS:
                self.logger.error(f"Communication error: {self.packet_handler.getTxRxResult(result)}")
                return False

            if error != 0:
                self.logger.error(f"Servo error: {self.packet_handler.getRxPacketError(error)}")
                return False

            self.logger.info(f"Moving to {angle:.1f}° (position {goal_position})")
            return True

        except Exception as e:
            self.logger.error(f"Move command failed: {e}")
            return False

    def get_status(self) -> Optional[dict]:
        """
        Get current servo status and telemetry

        Returns:
            dict: Status information or None if error
        """
        if not self.is_connected:
            return None

        try:
            # Current position
            position, _, _ = self.packet_handler.ReadPos(self.config.STS_ID)
            degrees = self.position_to_degrees(position)

            # Current draw
            current_raw, _, _ = self.packet_handler.read2ByteTxRx(self.config.STS_ID, 69)
            current = self.packet_handler.sts_tohost(current_raw, 15)
            current_mA = current * self.config.LSB_TO_mA

            # Supply voltage
            voltage_raw, _, _ = self.packet_handler.read1ByteTxRx(self.config.STS_ID, 62)
            voltage = voltage_raw * self.config.VOLTAGE_SCALE

            # Load percentage
            load_raw, _, _ = self.packet_handler.read2ByteTxRx(self.config.STS_ID, 60)
            load_percent = int(round(load_raw * self.config.LOAD_SCALE))

            # Temperature
            temperature, _, _ = self.packet_handler.read1ByteTxRx(self.config.STS_ID, 63)

            # Movement status
            is_moving, _, _ = self.packet_handler.ReadMoving(self.config.STS_ID)

            return {
                'position': position,
                'degrees': degrees,
                'current_raw': current,
                'current_mA': current_mA,
                'voltage': voltage,
                'load_percent': load_percent,
                'temperature': temperature,
                'is_moving': bool(is_moving)
            }

        except Exception as e:
            self.logger.error(f"Status read failed: {e}")
            return None

    def wait_for_completion(self, target_position: int, timeout: float = 10.0) -> bool:
        """
        Wait for movement to complete with real-time monitoring

        Args:
            target_position: Expected final position
            timeout: Maximum wait time in seconds

        Returns:
            bool: True if movement completed successfully
        """
        start_time = time.time()

        print("🟡 Movement in progress... (Press Ctrl+C to stop)\n")

        try:
            while time.time() - start_time < timeout:
                time.sleep(self.config.MONITOR_INTERVAL)

                status = self.get_status()
                if not status:
                    return False

                # Display status
                print(f" → Target: {target_position:4d} | "
                      f"Position: {status['position']:4d} ({status['degrees']:6.1f}°) | "
                      f"Current: {status['current_raw']:3d} ({status['current_mA']:.0f}mA) | "
                      f"Load: {status['load_percent']:2d}% | "
                      f"Temp: {status['temperature']}°C")

                # Safety checks
                if status['temperature'] > self.config.MAX_TEMPERATURE:
                    self.logger.warning(f"High temperature: {status['temperature']}°C")

                if status['current_mA'] > self.config.MAX_CURRENT:
                    self.logger.warning(f"High current: {status['current_mA']:.0f}mA")

                # Check if movement completed
                if not status['is_moving']:
                    print("✅ Movement completed\n")
                    return True

            self.logger.warning("Movement timeout")
            return False

        except KeyboardInterrupt:
            print("\n⏹️ Movement interrupted by user")
            return False

    def interactive_control(self):
        """Run interactive control interface"""
        print("\n" + "="*60)
        print("🤖 PARALLEL GRIPPER CONTROL INTERFACE")
        print("="*60)
        print(f"Servo ID: {self.config.STS_ID}")
        print(f"Port: {self.config.DEVICENAME}")
        print(f"Baud Rate: {self.config.BAUDRATE}")
        print("-"*60)
        print("Commands:")
        print("  • Enter angle in degrees (positive or negative)")
        print("  • Press Enter (empty) to exit")
        print("  • Ctrl+C to interrupt movement")
        print("="*60)

        try:
            while True:
                user_input = input("\nEnter target angle (degrees): ").strip()

                if not user_input:
                    print("👋 Exiting...")
                    break

                try:
                    angle = float(user_input)
                    target_position = self.degrees_to_position(angle)

                    if self.move_to_angle(angle):
                        self.wait_for_completion(target_position)

                except ValueError:
                    print("❌ Invalid input. Please enter a number.")
                except Exception as e:
                    self.logger.error(f"Control error: {e}")

        except KeyboardInterrupt:
            print("\n👋 Control interface interrupted")

def main():
    """Main function - entry point for the application"""
    print("🚀 Starting Parallel Gripper Control Software...")

    # Create gripper instance
    gripper = ParallelGripper()

    try:
        # Connect to servo
        if not gripper.connect():
            print("❌ Failed to connect to servo. Please check:")
            print("  • Port name (currently: {})".format(gripper.config.DEVICENAME))
            print("  • Servo power and connections")
            print("  • Servo ID (currently: {})".format(gripper.config.STS_ID))
            print("  • Baud rate (currently: {})".format(gripper.config.BAUDRATE))
            return 1

        # Run interactive control
        gripper.interactive_control()

    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return 1

    finally:
        # Ensure clean shutdown
        gripper.disconnect()

    return 0

if __name__ == "__main__":
    sys.exit(main())
