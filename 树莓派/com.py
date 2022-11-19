# -*- coding:utf-8 -*-
import serial
import time

#模式1：直通模式
mode_1 = [0x55,0xAA,0xAA,0x5A]
#模式2：整合模式（模块输出=pi输出+超声波输出）
mode_2 = [0x55,0xAA,0xA5,0xAA]

port = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=1.0)
uartMode = 1

def init(mode=1):
    global port
    global uartMode
    global mode_1,mode_2
    uartMode=mode
    mode_1 = bytearray(mode_1)
    mode_2 = bytearray(mode_2)
    port = serial.Serial("/dev/ttyAMA0", 115200, timeout=1.0)
    time.sleep(0.2)
    if(mode==1):
        port.write(mode_1)
    else:
        port.write(mode_2)
    time.sleep(1)

def send(data):
    #print uartMode
    if(uartMode>=2):
        if(len(data)>16):
            raise RuntimeError('In uart of mode_2,data length can\'t be larger than 16.')
    port.write(data)
