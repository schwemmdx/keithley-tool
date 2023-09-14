from time import sleep
from datetime import datetime
from keithley_lib import K2636
from keithley_dipshit import theme

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


k = K2636(ip='192.168.0.56',debug=False)

print("Attached Device:\n"+'-'*80)
print("On IP: "+k.tcpIp+'::'+str(k.tcpSock.INSTR_PORT))
info= k.getDeviceInfo()
for key in info:
    print(key+': '+info[key])
print('-'*80)
#k.clearDisplayMsg()
#k.tcpSock.write("smua.source.levelv=10")
#k.write_digIO(1,True)

k.reset()
k.welcome()
nErrors = k.error_queue.get_length()
print("Number or Errors in Queue: "+str(nErrors))
if(nErrors):
    errors = k.error_queue.read_all()
    for error in errors:
        print(error)
        

# #k.smu.source.func(k.smua.measure.FUNC_DC_CURRENT)
k.setIntegrationTime('smua',K2636.NPLC_HI_ACC/50)
k.smua.measure.autorangeI(1)
k.smua.measure.autorangeV(1)


print("\nPerforming > Basic Measurement Loop <")
print("Measurement Results\n"+'-'*80)


with open("testfile.csv",'w') as outFile:

    headerStr = "Time,Voltage,Current,Power,Resistance"
    unitStr = "[HH:MM:SS],[V],[A],[W],[Ohm]"
    fancyLine = '-'*80
    print((headerStr.replace(',','\t').expandtabs(16)+'\n'+unitStr.replace(',','\t').expandtabs(16)+'\n'+fancyLine))
    outFile.write((headerStr+'\n'+unitStr+'\n'))
    
    for setPoint in np.linspace(0,1e-2,num=200):
        k.applyCurrent('smua',setPoint,1,iRange='auto',vRange='auto')
        
        tStamp = datetime.now().strftime("%H:%M:%S")
        v = k.smua.measure.v()
       
        i = k.smua.measure.i()
    
        p = k.smua.measure.p()
       
        r =k.smua.measure.r()
        ataLine = f"{tStamp}\t{(v)}\t{(i)}\t{(p)}\t{(r)}"
        print(dataLine)

        dataLine = f"{tStamp}\t{float(v)}\t{float(i)}\t{float(p)}\t{float(r)}"
        outFile.write(dataLine.replace('\t',',')+"\n")
        print(dataLine)
        
        

k.reset()
theme(k)
# # df = pd.read_csv("testfile.csv")
# # df.drop(axis=0,index=0,inplace=True)
# # y = df['Current'].to_numpy().astype(float)
# # plt.plot(range(testtime),y,marker='o',markerfacecolor='None',c='tab:blue')
# # plt.ylabel("Current $I_{SMUA}$ [A]")
# # plt.ylim(min(y),max(y))
# # plt.xlabel("Measurement #")

# # plt.show()