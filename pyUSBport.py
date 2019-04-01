import serial
from serial import Serial
import time
import cv2
import threading
import os
 
def show_webcam(ser_id, mirror=False):
    counter = 1
    cam = cv2.VideoCapture(0) # change the device id to your camera
    while True:
        ret_val, img = cam.read()
        if mirror: 
            img = cv2.flip(img, 1)
        cv2.imshow('my webcam', img)
        key = cv2.waitKey(1)
        if key == 27: 
            break  
        elif key == ord('s'):
            cv2.imwrite('images/' + str(counter) + '.png',img)
            counter += 1
        elif key == ord('t'):
	    # change this line to whatever u want to send
            ser_id.write(b"CT+TRUNSINGLE(1,45);")

        
    cv2.destroyAllWindows()
   

def main():
    if not os.path.exists('images'):
        os.mkdir('images')
        
    ser = serial.Serial()
    ser.baudrate = 115200
	# change to your port
    ser.port = 'COM3' # /dev/ttyUSB0 for linux 
    ser.open()
    ser.parity = serial.PARITY_NONE
    ser.BYTESIZES = serial.EIGHTBITS
    ser.STOPBITS = serial.STOPBITS_ONE
    ser.timeout = 1000

    show_webcam(ser, mirror=True)

    # this is for listening to the heartbeat 
    #s = ser.read(1)
    #print(s)

    ser.close()   

if __name__ == '__main__':
    main()

