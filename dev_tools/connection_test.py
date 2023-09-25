from modules.keithley_lib import K2636


k = K2636()
k.tcpConnect("192.168.0.56",5025)

k.display.setText("Test")
