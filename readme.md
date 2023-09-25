# keithley-tool

## For What Hardware it's used?
Short Answer: for my personal K2636A SMU, but because of Keithley's TSP Language most 26XX Models should work just fine. The Console Works for all TCP Connections btw (but probably an shell tool works better :/)

## Why another Keithley Tool?
Ya, well .... ill got one for private reasons and no acess to a proper lab-bech power supply- thats the background of it.
In order to use the SMU's as independent Voltage/Current Sources with graphical feedback for drawn current or voltage levels this tool was created.

There are many projects out there using some sort of VISA Library... and for me VISA is not an option. DOnt get me wrong, ill respect the hard work and time it consumed to create `pyvisa` or similar approaches, but for me the most reliable connection for data transfer appeard to be raw sockets. 
(Also National Instruments is the devil :D)

## Planned functions 
- Basic Lab Bench Powersupply Mode with graphical measurements of currents, voltages, power and resistance
- Sweep Mode with One/Both SMUs for device characterisation
- Raw Console to communicate to Endpoint
- Error Widget for displaying internal errors
- Script Managment Helper to easily upload tsp-script and various data

## What library for communication is used?
Self written simple and lightweight class for basic interfacing.
>More Info is coming later :)
## What GUI Library is used?
I'll use PySide6 only for everything. The widgets are pretranslated from *.ui / *.qrc by running `build_tasks.py`, so no dynamic loading dishittery.


