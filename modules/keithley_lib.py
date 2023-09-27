from socket import *

import select
from time import sleep

import threading
from typing import Any

def get_default_channel_config():
    """"Standard Basic Configuration noeeded for the SMU CH to operate at a given Operation Point"""
    cfg = {
        'source':{
            'forcev' : True,
            'forcei' : False,
            'levelv' : 1,
            'limitv' : 1,
            'limiti' : 1e-3,
            'leveli' : 1e-3
        },           
        'measure':{
            'rangev': 'auto',
            'rangei':'auto',
            'interval': 1,
        }
    }
    return cfg



class K2636SubClass:
    """Base Class for all subclasses of SMU in order to mimic the LUA-like beaviour of referencing"""
    def __init__(self,tcpSock):
        self.sock = tcpSock
    
    


class TCPInstr:
    INSTR_PORT = 5025
    """Lower Level TCP Socket Handling for TCP-Connected Instruments
    Handling is done without any VISA Connection"""
    def __init__(self,debug = False):

        self.debug = debug
        
        self.timeout_s = 5.
       
        self.readbuf = []
        self.recvbuf = b''

        self.line = 0
        self.connectionStatus = False


    def write(self, s,):
        if not len(s):
            return False
        if s.replace(' ', '')[0:2] == '--':
            return False

        self.line += 1
        #print '%3d: %s' %(self.line, s)
        if self.debug:
            print("Send -> \t "+s)
        
        self.sock.sendall(s.encode() + b'\n')
        
    def read(self):
        if self.connectionStatus:
            if not len(self.readbuf):
                # read with timout
                waitForData = True
                while waitForData:
                    ready = select.select([ self.sock ], [], [], self.timeout_s)
                    if ready[0]:
                        self.recvbuf = self.sock.recv(1024)
                        #print(self.recvbuf)
                        waitForData = False
                    else:
                        print('Timeout occured reading data from TCP Socket')
                        return ''

                # read without timeout
                #self.recvbuf += self.sock.recv(1024)
                i = self.recvbuf.rfind(b'\n')
                self.readbuf = self.recvbuf[:i].split(b'\n')
                self.recvbuf = self.recvbuf[i+1:]

            s = self.readbuf[0]
            del self.readbuf[0]
            # print(s.decode())

            return s.decode()

    def query(self,cmd):
        
        self.write(cmd)
        return self.read()


    def close(self):
        self.sock.close()
        self.connectionStatus = False

    def connect_to(self,ip,port,timeout = 1000):
        self.portUsed = port
        self.ipUsed = ip
        self.timeout_s = timeout/1e3
        
    
        self.sock = socket()

        self.sock.connect((self.ipUsed,self.portUsed))
        self.sock.settimeout(int(self.timeout_s))
        self.sock.setsockopt(IPPROTO_TCP,TCP_NODELAY,1024)
        self.connectionStatus = True
        

class Source:
    def __init__(self,smuName,sock) -> None:
        self.name = smuName
        self.sock = sock
        self.out_type = 'OUTPUT_DCAMPS'


    def rangei(self,rangeI):
        self.sock.write(self.name+'.source.rangei='+str(rangeI))

    def rangev(self,rangeV):
        self.sock.write(self.name+'.source.rangev='+str(rangeV))
    
    def limitv(self,limitV):
        self.sock.write(self.name+'.source.limitv='+str(limitV))
    
    def limiti(self,limitI):
        self.sock.write(self.name+'.source.limiti='+str(limitI))



    def func(self,tp):
        self.sock.write(self.name+'.source.func = '+str(tp))
        

    def output(self,state):
        if state:
            state=1
        else:
            state=0
        self.sock.write(self.name+'.source.output='+str(state))

    def levelv(self, voltage):
        self.sock.write(self.name+'.source.levelv='+str(voltage))

    def leveli(self, current):
        self.sock.write(self.name+'.source.leveli='+"{:.4e}".format(current))


    def isCompliance(self):
        pass

class Measure:
    FUNC_DC_CURRENT = 'FUNC_DC_CURRENT'

    def __init__(self,smuName,sock):
        self.smuName = smuName
        self.sock = sock

    def func(self,typ):
        self.sock.write(self.smuName+".measure.func = smu."+typ)
        
    def i(self,n=1):
        self.sock.write('i = '+self.smuName+'.measure.i()\nprint(i)')
        return self.sock.read()

    def v(self,n=1):
        #self.sock.write(self.smuName+'.count = '+str(n))
        self.sock.write('v = '+self.smuName+'.'+'measure.v()\nprint(v)')
        return self.sock.read()

    def iv(self,n=1):
        #self.sock.write(self.smuName+'.count = '+str(n))
        self.sock.write('a,b = '+self.smuName+'.'+'measure.iv()\nprint(a,b)')
        val = self.sock.read()
        i,v = val.split('\t')
        return (i,v)

    def p(self,n=1):
        #self.sock.write(self.smuName+'.count = '+str(n))
        self.sock.write('p = '+self.smuName+'.'+'measure.p()\nprint(p)')
        val = self.sock.read()
        return val

    def r(self,n=1):
        #self.sock.write(self.smuName+'.count = '+str(n))
        self.sock.write('r = '+self.smuName+'.'+'measure.r() print(r)')
        return self.sock.read()

    def autorangeI(self,state):
        self.sock.write(self.smuName+".measure.autorangei ="+str(state))

    def autorangeV(self,state):
        self.sock.write(self.smuName+".measure.autorangev ="+str(state))
        
    def rangeI(self,ran):
        self.sock.write(self.smuName+".measure.rangei ="+str(ran))
    def rangeV(self,ran):
        self.sock.write(self.smuName+".measure.rangev ="+str(ran))
        
    def nplc(self,val):
        if not 0.001 <= val <= 25:
            print(f"{val} is not valid for number of power cycles!")
            raise ValueError
        else:
            self.sock.write(self.smuName+'.measure.nplc='+str(val))



class SMU:
   
    def __init__(self,name,sock,**kwargs):
        self.name = name
        self.sock = sock
        self.measure = Measure(name,self.sock)
        self.source = Source(name,self.sock)
    
    def reset(self):
        self.sock.write(f"{self.name}.reset()")

class KeithleyError:
    
    def __init__(self,rawStr):
        errorCode,message,severity,node = rawStr.split('\t')
        self.error_code = int(float(errorCode))
        self.message = message
        self.severity = int(float(severity))
        self.node = int(float(node))
        
    
    def __str__(self):
        return f"{self.error_code}\t{self.message}\t{self.severity}\t{self.node}"
          
class Errorqueue(K2636SubClass):
    def __init__(self, tcpSock):
        super().__init__(tcpSock)
        self.error_dump = []

    def get_length(self):
        numErrors = self.sock.query('print(errorqueue.count)')
        numErrors = int(float(numErrors))
        return numErrors
     
    def read_all(self,autosave=True,save_location='error_dump.log'):
        numErrors = self.get_length()
        
        if numErrors:
            for i in range(numErrors):
                ans = self.sock.query('print(errorqueue.next())')
                self.error_dump.append(KeithleyError(ans))
        if autosave:
            self.save_to_disk(save_location)
            
        return self.error_dump    

    def save_to_disk(self,location):
        with open(location,'w') as dumpFile:
            for err in self.error_dump:
                dumpFile.write(str(err)+'\n')


class Display(K2636SubClass):
    
    def __init__(self, tcpSock):
        super().__init__(tcpSock) 
        
    def clear(self):        
        self.tcpSock.write('display.clear()')

    def setText(self,string):
        self.tcpSock.write('display.settext("'+string+'")')
    
    def setMeasureFunc(self,smu,func=0):
# 0 or display.MEASURE_DCAMPS: Selects current measure function
# 1 or display.MEASURE_DCVOLTS: Selects volts measure function
# 2 or display.MEASURE_OHMS: Selects ohms measure function
# 3 or display.MEASURE_WATTS: Selects power measure function
        self.sock.write('display.'+smu+'.measure.func = '+str(func))
        
    def setNumDigits(self,smu,num=5):
        self.sock.write('display.'+smu+'.digits = '+str(num))
         
            

class K2636:
    NPLC_FAST = 0.01
    NPLC_MED = 0.1
    NPLC_NORM = 1
    NPLC_HI_ACC = 10
    
    DISP_MEAS_FUNC_AMP = 0
    DISP_MEAS_FUNC_DCVOLTS = 1
    DISP_MEAS_FUNC_OHMS = 2
    DISP_MEAS_FUNC_WATTS = 3
    
    SMUA = 'smua'
    SMUB = 'smub'
    OUTPUT_DCAMPS = 0
    OUTPUT_DCVOLTS = 1

    def __init__(self,ip='192.168.0.056',debug = False):
        self.tcpIp = ip
        self.tcpSock = TCPInstr(debug=debug)
        self.error_queue = Errorqueue(self.tcpSock)
        self.display = Display(self.tcpSock)
        self.smua = SMU('smua',self.tcpSock)
        self.smub = SMU('smub',self.tcpSock)

    def tcpConnect(self,ip,port,timeout=1000):
        """Connects to the provided tcp endpoint"""
        self.tcpSock.connect_to(ip,port,timeout)

    def reset(self):
        """Resets the instrument"""
        self.tcpSock.write('reset()')

    def isConnected(self):
        return self.tcpSock.connectionStatus

    def getDeviceInfo(self):
            
        """Reads the SCIPI like *IDN? command from the connected socket, if possible and tries to 
        fit in into Keithley-like formatted dict
        """
        try:
            self.tcpSock.write('*IDN?')
            retStr = self.tcpSock.read(1)
        except:
            retStr = 'None,None,-1,-1'
        buf = retStr.split(',')
        idData = {}
        idData['Manufacturer'] = buf[0]
        idData['Type'] = buf[1]
        idData['HW. Rev.'] = buf[2]
        idData['SW. Rev.'] = buf[3]
        return idData

    def write_digIO(self,pin,state=True):
        """Sets the Digital IO-Line <pin> to <state>"""
        if state:
            state=1
        else:
            state=0
        

        self.tcpSock.write('digio.writebit('+str(pin)+','+str(state)+')') 

    def read_digIO(self):
        return self.query('port = digio.readport()\n print(port)') 

    def beep(self,t,f):
        self.tcpSock.write("beeper.enable = beeper.ON")
        self.tcpSock.write("beeper.beep("+str(t)+","+str(f)+")")

    def fanfareConnect(self):
        self.beep(0.1,600)
        self.beep(0.1,1200)
        self.beep(0.25,2400)
    
    def fanfareDisonnect(self):
        self.beep(0.1,2400)
        self.beep(0.1,1200)
        self.beep(0.25,600)



    def _veritfySmuName(self,name):
        smu = name.lower().strip(' ')
        if smu == K2636.SMUA:
            s = self.smua
        elif smu == K2636.SMUB:
            s= self.smub
        else:
            raise NotImplementedError
        return s
    def _verifyRangeInput(self,s,iRange,vRange):
        if not iRange.lower() =='auto':
            s.measure.rangeI(str(iRange))
        else:
           
            s.measure.autorangeI(1)
        
        if not vRange.lower() == 'auto':
            s.measure.rangeV(str(vRange))
        else:
            s.measure.autorangeV(1)
            
    def applyConfig(self,smuName,cfg):
        """Sends the given Config via the underlying tcp socket to the intrument"""
        src = cfg['source']
        meas = cfg['measure']
        if cfg['source']['forcev']:
            #voltage is force
            self.applyVoltage(smuName,src['levelv'],src['limiti'],meas['rangei'],meas['rangev'])
        else:
            #current is force
            self.applyCurrent(smuName,src['leveli'],src['limitv'],meas['rangei'],meas['rangev'])
        


     
    def setIntegrationTime(self,smu,tInt,fLine=50):
        """Set's the <smu>'s integration time <tInt> to the desired value.
        The internal ADC of the K2600 series adc's rely entirely on NPLC- Number of Power Line Cycles.
        The boundries of NPLC are:
            0.001 < NPLC < 25
        
        Therefore the Power Line frequency (usually 50 Hz) creates the following boundries
        
            0.001/f < NPLC < 25/f

            2e-5 s < tInt < 0.5s
            
         """
        
        s= self._veritfySmuName(smu)
        s.measure.nplc(tInt*fLine)
               
    def applyVoltage(self,smu,volts,ilim=1e-2,iRange='auto',vRange='auto'):
        """Simple High Level API to apply a voltage level <volts> to an SMU (a or b)
        The underlying handling for range and limits are derived from the given input
        """
     
        s = self._veritfySmuName(smu)
        self.display.setMeasureFunc(s.name,K2636.DISP_MEAS_FUNC_AMP)
        self.display.setNumDigits(s.name,6)
          
        s.source.rangev(volts)
        s.source.func(K2636.OUTPUT_DCVOLTS)
        self._verifyRangeInput(s,iRange,vRange)
        s.source.limiti(ilim)
        
        s.source.levelv(volts)
        
        
    def applyCurrent(self,smu,amps,vlim=1,vRange='auto',iRange='auto'):
        """Simple High Level API to apply a current level <amps> to an SMU (a or b)
        The underlying handling for range and limits are derived from the given input
        """
        
       
        s = self._veritfySmuName(smu)
        self.display.setMeasureFunc(s.name,K2636.DISP_MEAS_FUNC_DCVOLTS)
        self.display.setNumDigits(s.name,6)
        
        s.source.rangei(amps)
        s.source.func(K2636.OUTPUT_DCAMPS)
        self._verifyRangeInput(s,iRange,vRange)
        s.source.limitv(vlim)
        s.source.leveli(amps)
            
    def measure(self,smuName,params):
        if smuName == 'smua':
            smu =self.smua
        elif smuName == 'smub':
            smu = self.smub  
    
        results = {}
        
        for param in params:
            if param == 'v':
                func = smu.measure.v
            elif param == 'i':
                func = smu.measure.i
            elif param =='r':
                func = smu.measure.r
            elif param == 'p':
                func = smu.measure.p
    
            results[param] = func()
        return results

    def setOutput(self,smuName:str,state:bool):
        if state:
            state = 1
        else: 
            state = 0
            
        """Sets the Output of <smuName> to <state>"""
        self.tcpSock.write(smuName+'.source.output='+str(state))

    
    def check_errors(self):
        num = self.error_queue.get_length()
        if num:
            return True
        else:
            return False

    def readErrors(self,autosave=False,save_location='error_dump.log'):
        return self.error_queue.read_all(autosave=autosave,save_location=save_location)
    
    
