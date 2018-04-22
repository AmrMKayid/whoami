import serial
ser = serial.Serial('/dev/tty.usbmodem1421', 9600)

i = 5
while i > 0:
    ser.write(b'1')
    i -= 1
    ser.write(b'1')
    if(ser.readline() == b'1\r\n'):
        break