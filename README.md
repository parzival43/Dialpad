# Dialpad — Custom Macropad

A custom-designed macropad built around the **Seeed Studio XIAO RP2040**, featuring 12 mechanical keys, two rotary controls, a joystick, and a display. Designed with KiCad and Fusion 360, Dialpad brings programmable inputs into a compact, customizable desktop device.

## Overview

Dialpad is a custom macropad designed to make frequently used shortcuts and controls more accessible. It combines mechanical switches with rotary controls, a joystick, and a display in a single device.

The project includes a custom PCB and schematic, a 3D-designed enclosure, and firmware for handling the inputs.

### Features

- **12 mechanical keys** for shortcuts and custom actions
- **2 rotary controls** for adjustable parameters and navigation
- **1 joystick** for directional input
- **Display** for visual feedback
- **XIAO RP2040** as the main microcontroller
- Custom PCB designed in KiCad
- Custom enclosure designed in Fusion 360
- Custom micropython firmware with serial communicaiton

## Project Gallery

### 1. Complete Macropad

![Dialpad overview](Photos/dialpad.png)

*Overall design of the Dialpad macropad.*

### 2. Schematic

![Dialpad schematic](Photos/schematic_photo.webp)

*Electrical schematic for the macropad.*

### 3. PCB Layout

<!-- Add a screenshot of the PCB layout exported from KiCad. -->
![Dialpad PCB layout](Photos/Kicad_layout_photo.png)

*Custom PCB layout, including the microcontroller and input circuitry.*

### 4. Case Design and Assembly

<!-- Add a Fusion 360 screenshot showing the assembled case and how its parts fit together. -->
![Dialpad case assembly](Photos/case.png)
![Dialpad case fitting](Photos/fitting.png)

*CAD assembly showing the enclosure, PCB placement, and how the case parts fit together.*

## Bill of Materials (BOM)

The following is the preliminary component list. Verify exact part numbers, resistor values, and quantities against the final schematic and PCB before ordering.

| Component | Quantity | Purpose |
|---|---:|---|
| Seeed Studio XIAO RP2040 | 1 | Main microcontroller |
| Mechanical key switches | 12 | Primary key inputs |
| Rotary encoders | 2 | Rotary input and adjustment |
| Joystick module | 1 | Directional input |
| Display module | 1 | Visual feedback |
| PCB | 1 | Main circuit board |
| Resistors | As required | Input circuitry |
| USB cable | 1 | Power and USB connection |
| 3D-printed enclosure | 1 set | Protects and supports the electronics |
| Keycaps | 12 | Key tops |
| Knobs | 2 | Rotary encoder controls |
| Mounting hardware | As required | Secures the PCB and enclosure |

*Note: Confirm the exact display, joystick, encoder, switch, resistor, and mounting-hardware specifications before manufacturing.*

## Repository Structure

```text
Dialpad/
├── CAD/
│   └── Complete case assembly (STEP/STP/3MF)
├── PCB/
│   ├── KiCad project file (.kicad_pro)
│   ├── Schematic file (.kicad_sch)
│   └── PCB layout file (.kicad_pcb)
├── Firmware/
│   └── Firmware source files
├── production/
│   ├── gerbers.zip
│   ├── Case manufacturing files (STEP/STL)
│   └── Firmware build (if applicable)
├── assets/
│   ├── pcb_layout.png
│   └── case_assembly.png
├── dialpad.png
├── Kicad_schematic_photo.png
└── README.md
```

*The tree above describes the intended organization. Keep only the filenames and files that actually exist in the repository, and add any missing production files before submission.*

## Design Tools

- **KiCad** — schematic capture and PCB design
- **Fusion 360** — enclosure design and CAD assembly
- **MicroPython** — firmware development, if using the current MicroPython implementation

## Building and Usage

1. Review the schematic and PCB source files in `PCB/`.
2. Open the CAD assembly in `CAD/` to inspect the enclosure and component placement.
3. Follow the instructions and source files in `Firmware/` to set up the firmware.
4. Connect the macropad to a computer using USB once the hardware and firmware are ready.

Detailed flashing instructions and key mappings will be documented here after the firmware implementation is finalized.

## Project Status

The PCB design has been developed, and the enclosure and firmware are part of the project workflow. Hardware assembly and final functional testing should be completed before describing the macropad as fully operational.

## Acknowledgements

Created as part of the Hackpad project by Hack Club.

---

**Repository:** [parzival43/Dialpad](https://github.com/parzival43/Dialpad)