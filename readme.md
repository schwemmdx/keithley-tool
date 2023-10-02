# keithley-tool
![Qt](https://img.shields.io/badge/Qt-%23217346.svg?style=for-the-badge&logo=Qt&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black) ![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white) 


## For What Hardware it's used?
Short Answer: for my personal K2636A SMU, but because of Keithley's TSP Language most 26XX Models should work just fine. The Console Works for all TCP Connections btw (but probably an shell tool works better :/)

## Why another Keithley Tool?!

Ya, well .... ill got one for private reasons and no acess to a proper lab-bech power supply- thats the background of it.
In order to use the SMU's as independent Voltage/Current Sources with graphical feedback for drawn current or voltage levels this tool was created.

There are many projects out there using some sort of VISA Library... and for me VISA is not an option. Dont get me wrong, ill respect the hard work and time it consumed to create `pyvisa` or similar approaches, but for me the most reliable connection for data transfer appeard to be raw sockets. 
(Also National Instruments is the devil :D)

## Planned functions 
- [x] Basic Lab Bench Powersupply Mode with graphical measurements of currents, voltages
![basic_view](https://github.com/schwemmdx/keithley-tool/assets/57574663/46a19792-35c9-47ca-820f-30196fc37f08)

- [x] Raw Console to communicate to Endpoint
![console_view](https://github.com/schwemmdx/keithley-tool/assets/57574663/c41354c2-9850-4864-b35d-f994eaf35206)

- [X] Error Widget for displaying internal errors
![error_view](https://github.com/schwemmdx/keithley-tool/assets/57574663/ad666715-cfb0-4e0b-b77b-34f01232605f)


- [ ] Sweep Mode with One/Both SMUs for device characterisation 
- [ ] Script Managment Helper to easily upload tsp-script and various data

## What library for communication is used?
Self written simple and lightweight class for basic interfacing.
>More Info is coming later :)
>
## What GUI Library is used?
I'll use PySide6 only for everything. 

## Build and run
The widgets are pretranslated from *.ui / *.qrc by running 
```
build_tasks.py
```
So no dynamic loading. 
Then just run the application with 
```
python ./main.py
```

## Materials and Art
The used materials and icons are from _FreePic_ sourced via [flaticon](https://www.flaticon.com/de/autoren/special/lineal-color/14)
