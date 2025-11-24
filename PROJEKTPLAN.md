# Projektplan — Grabbot (Bildungsprojekt)

MVP
- Teleoperation: Laptop sendet Kommandos → Arduino/ESP32 steuert Motoren → Greifer hebt Objekt von A nach B.

Meilensteine
1. Konstruktion Chassis in Blender (2 Wochen) — 3d-Druck mit Ultimaker Cura
2. BOM (Bill of Materials) & Motorauswahl (1 Woche)
3. Elektrik & Prototypaufbau (1–2 Wochen)
4. Firmware (Arduino): Basis‑API über Serial (2 Wochen)
5. Python Control App (2–3 Wochen)
6. Tests (solange wie die Lust reicht)

Starter‑Aufgaben (Beispiele)
- Motoren auswählen, Einkaufsliste erstellen
- Entwurf serielles Protokoll (Arduino ↔ Laptop)
- Minimal‑Arduino‑Sketch für PWM/Servo
- Python Teleop CLI

Testplan
- 50x Greifversuche per Teleop, Ziel: Erfolgsrate ≥ 80% für MVP
