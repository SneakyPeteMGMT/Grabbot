# Grabbot — Bildungsprojekt: Roboter mit Greifarm

Kurzbeschreibung
----------------
Grabbot ist ein Bildungsprojekt, das Lernenden praktische Erfahrung in eingebetteter Elektronik, Steuerung, Programmierung und Robotik vermittelt. Ziel ist ein einfacher Greifarm, der über einen Laptop gesteuert wird (Python) und über ESP32 / Arduino kommuniziert.

Projektziele
- Lernziele: Serielle/WiFi‑Kommunikation, Motorsteuerung, einfache Kinematik, Debugging‑Workflows.
- MVP: Teleoperation: Greifer bewegt einen standardisierten Würfel (z. B. 3×3×3 cm) von A nach B.
- Erweiterung: Sequenzen, einfache Vision (optional).

Hardware (derzeit)
- ESP32 (Kommunikation / Telemetrie)
- Arduino Uno (Low‑level I/O, PWM)
- Diverse Bauteile (Kabel, Widerstände, Transformatoren)
- Motoren: noch zu beschaffen (Vorschläge in PROJEKTPLAN.md)

Software
- Steuerung: Laptop (Python)
- Low‑level: Arduino IDE / ESP32 Firmware (falls benötigt)

Ordnerstruktur 
- layout/          - Schaltpläne
- Construction     - Konstruktionspläne Blender/.stl
- src/             — Python Control App, Scripts
- firmware/        — Arduino/ESP32 Sketche

Erste Schritte
1. Konstruktion Chassis
2. BOM vervollständigen (Motoren auswählen).
3. Basisverkabelung dokumentieren.
4. Firmware‑Stubs: serielles Protokoll definieren (z. B. newline‑terminated JSON).
5. Python‑Teleop: CLI/GUI für manuelle Sequenzen.

Lizenz
- MIT (siehe LICENSE)
