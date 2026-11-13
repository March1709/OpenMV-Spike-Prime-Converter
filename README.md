# OpenMV-Spike-Prime-Converter

This project includes a circuit board, mounting accessories, and sample programs that enable OpenMV to be used with LEGO SPIKE Prime by attaching the board to the ultrasonic sensor housing.

The hardware is released as open-source hardware under the Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) license.

- [Open Source Hardware Definition](https://www.oshwa.org/definition/)
- [CC BY-SA 4.0 License](https://creativecommons.org/licenses/by-sa/4.0/)

## File Descriptions

### Hardware

- **board.brd**: An EAGLE-compatible PCB layout file.
- **schematic.sch**: An EAGLE-compatible schematic file.
- **spacer_FRONT**: A spacer used on the front side of the PCB. Insert its protrusions into the outer holes of the PCB, then fix the assembly using the screws that originally held the ultrasonic sensor module in place.
- **spacer_BACK**: A spacer used on the back side of the PCB. Insert its protrusions into the inner holes of the PCB to set the proper distance between the PCB and the ultrasonic sensor housing.

### Sample Programs

- **OpenMV_sample.py**: Sends the number `100` from OpenMV to SPIKE Prime once per second.
- **SPIKE_sample.llsp**: Displays the data received by SPIKE Prime in the console.

## Assembly Instructions

Refer to `mount_example.step` for an example of the assembled hardware.

## License

The hardware design files and mounting accessories are licensed under the Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) license.

- [CC BY-SA 4.0 License](https://creativecommons.org/licenses/by-sa/4.0/)

## Questions and Issues

If you have any questions or encounter any problems, please open an issue in the GitHub Issues section.
