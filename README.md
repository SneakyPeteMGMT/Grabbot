# Grabbot — Educational project: robot with gripper arm

Short description
-----------------
Grabbot is an educational project that gives learners practical experience in embedded electronics, control, programming, and robotics. The goal is a simple gripper arm that can be controlled by a laptop [...].

Project goals
- Learning objectives: serial/WiFi communication, motor control, basic kinematics, debugging workflows.
- MVP: Teleoperation — gripper moves a standardized cube (e.g., 3×3×3 cm) from A to B.
- Extension: sequences, simple vision (optional).

Hardware (current)
- ESP32 (communication / telemetry)
- Arduino Uno (low-level I/O, PWM)
- Various components (wires, resistors, transformers)
- Motors

Software
- Control: Laptop (Python)
- Low-level: Arduino IDE / ESP32 firmware (if needed)
- Blender
- Ultimaker Cura

Folder structure
- layout/          - circuit diagrams
- Construction     - construction plans (Blender / .stl)
- src/             — Python control app, scripts
- firmware/        — Arduino / ESP32 sketches

First steps
1. Build chassis
2. Complete BOM (choose motors)
3. Document basic wiring
4. Firmware stubs: define serial protocol (e.g., newline-terminated JSON)
5. Python teleop: CLI/GUI for manual sequences

License
- MIT (see LICENSE)
