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
   ![image](https://github.com/schwemmdx/keithley-tool/assets/57574663/807e71a3-2b75-4608-8722-d4f353bf9298)


- [x] Sweep Mode with One/Both SMUs for device characterisation
![Bildschirmfoto vom 2023-11-10 21-00-00](https://github.com/schwemmdx/keithley-tool/assets/57574663/580088ce-4cb5-4d38-978e-f1ab48ba3ffb)

- [ ] Script Managment Helper to easily upload tsp-script and various data

## What library for communication is used?
### Overview
Similar to the lua scripting concept of the interla tsp language, ill tried to stick to the coding scheme with the keithley-tool tibrary.
The Main Class used is `K2636`with its multiple sub-classes 
a) `smua`
b) `smub`
c) `display`
d) `error_queue`
e) `tcpSock`

#### a) & b)
these are the _physical_ smu's inside the K2636 Housing. Each of them consists of an subclass `measure` and `source` with it's respective methods according to the reference manual (currently only a few a implemeted, but in the future maybe will be extended :) )
#### c)
According to the reference manual, these subclass represents the display object and also ... only a few methods are implemented till now.
#### d) 
Ahh... Yes... Errors!
Rather sophisticaed error handling is not what we are talking about. This class represents the error-queue on the K2636 device. The errors during operation are stored on it, can be gathered, thus automatically deleted on the K2636.
#### e)
The core of the library. Just a basic __tcp__ socket conneted to the `raw` port of the keithley's tcp socket. Usually the communication is done via ascii-strings. therefore everything is built on top of this communication class. Till now i wasn't able to coop with the lack of acknowledgement by the K2636, therefore it tries to read, directly after you send something out to the K2636, till an timeout occures.

You can also use the library for script based applications as follows:
```
from modules.keithley_lib import K2636

k = K2636()
k.tcpConnect("192.168.0.56",5025)
k.display.setText("Hello World")
```
This should set the displayed text to _hello woorld_ ... obviously!

```
from modules.keithley_lib import K2636,get_default_channel_config

k = K2636()
k.tcpConnect("192.168.0.56",5025)
k.applyVoltage("smua",1.25,ilim=1e-2)
k.setOutput('smua',True)
```
This applies 1.25 V with an comliance of 10 mA to SMUA. Because of electrical savety reasons, the output needs to be manually switched on. Dont worry, the interlock prevents voltages above 30V DC, if you didn't bridge the interlock on the K2636 manually.

```
results = k.measure('smua',['i','v'])

```
Measures the current and voltage on SMUA and returns a dictinary of the results requested by the parameter list provided.

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

## Whats next?
1. Multicolor Sweeps, for each SMUA Sweep, another color needs to be used (sounds simple, but because of bad code, a few things need to be thrown around :/ )
2. Some Settings that can be saved to disk and loaded again during startup of the application
