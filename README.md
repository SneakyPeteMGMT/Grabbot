# Grabbot — Bildungsprojekt: Roboter mit Greifarm

Kurzbeschreibung
----------------
Grabbot ist ein Bildungsprojekt, das Lernenden praktische Erfahrung in eingebetteter Elektronik, Steuerung, Programmierung und Robotik vermittelt. Ziel ist ein einfacher Greifarm, der über einen Laptop gesteuert wird (Python) und über ESP32 / Arduino kommuniziert.

Projektziele
- Lernziele: Serielle/WiFi‑Kommunikation, Motorsteuerung, einfache Kinematik, Debugging‑Workflows.
- MVP: Teleoperation: Greifer bewegt einen standardisierten Würfel (z. B. 3×3×3 cm) von A nach B.
- Erweiterung: Sequenzen, einfache Vision (optional), Übungsaufgaben für Lernende.

Hardware (derzeit)
- ESP32 (Kommunikation / Telemetrie)
- Arduino Uno (Low‑level I/O, PWM)
- Diverse Bauteile (Kabel, Widerstände, Transformatoren)
- Motoren: noch zu beschaffen (Vorschläge in PROJEKTPLAN.md)

Software
- Steuerung: Laptop (Python)
- Low‑level: Arduino IDE / ESP32 Firmware (falls benötigt)

Ordnerstruktur (Vorschlag)
- docs/            — Tutorials, How‑tos, Schaltpläne
- src/             — Python Control App, Scripts
- firmware/        — Arduino/ESP32 Sketche
- hw/              — BOM, Schaltpläne
- tests/           — Testskripte, Prüfprotokolle
- .github/         — Issue templates, workflows

Erste Schritte
1. BOM vervollständigen (Motoren auswählen).
2. Basisverkabelung dokumentieren.
3. Firmware‑Stubs: serielles Protokoll definieren (z. B. newline‑terminated JSON).
4. Python‑Teleop: CLI/GUI für manuelle Sequenzen.
5. Testplan & Übungen für Lernende erstellen.

Lizenz
- MIT (siehe LICENSE)