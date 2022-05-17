import time
import serial

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=115200,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
)


while 1 :
    raw=ser.readline().decode()
    pos=int(raw[9:17])
    diff=int(raw[24:-2])

    print(pos, ",",diff)
