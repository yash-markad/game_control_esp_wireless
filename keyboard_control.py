import serial
import time
import pyautogui

#set correct port and baudrate
ser = serial.Serial("COM4",115200,timeout=1)

while 1:
    
    dat = ser.readline()
    dat = dat.strip().decode()
    dat = dat.split(",")

    #dat shows the list of x and y element updated
    #do processing onward

    x = int(float(dat[0]))
    y = int(float(dat[1]))
    
    #Setting up the Keyboard controll over the gesture

    if 4000 < y < 5800:
        pyautogui.press('up')
        
    elif 7800< y  <9000:
        pyautogui.press('down')
    
    elif 8500<x<9400:
        pyautogui.press('right')
    
    elif 4700<x<6000:
        pyautogui.press('left')

    else :
        pass

        
ser.close()
