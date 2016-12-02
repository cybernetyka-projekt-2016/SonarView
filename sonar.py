import serial
import time
from socketIO_client import SocketIO, LoggingNamespace
socketIO = SocketIO('localhost', 5000, LoggingNamespace)
serialPort = serial.Serial(port="COM5",
                    baudrate=19200,
                    parity = serial.PARITY_NONE,
                    stopbits = serial.STOPBITS_ONE,
                    bytesize = serial.EIGHTBITS,
                    timeout = 2)

if(serialPort.isOpen() == False):
    serialPort.open()


serialPort.flushInput()
serialPort.flushOutput()

angle = 90
step = 2

while True:
    serialPort.write([255,angle])
    time.sleep(0.2)   
    if(serialPort.inWaiting() != 0):
        serialPort.read(6)
        s0_msb = int.from_bytes(serialPort.read(1), byteorder = "big", signed = False)
        s0_lsb = int.from_bytes(serialPort.read(1), byteorder = "big", signed = False)
        s1_msb = int.from_bytes(serialPort.read(1), byteorder = "big", signed = False)
        s1_lsb = int.from_bytes(serialPort.read(1), byteorder = "big", signed = False)
        s0_cm = (s0_msb*256 + s0_lsb)*2.54/4
        s1_cm = (s1_msb*256 + s1_lsb)*2.54/4
        # print ("S0: " + str(s0_cm) + " S1: " + str(s1_cm))
        print({angle:int(s0_cm)})
        if int(s0_cm) < 1000:
            socketIO.emit('measurement', {angle:int(s0_cm)})

    angle = angle + step
    if ((angle > 175) or (angle < 5)):
        step = -step
        
serialPort.close()
