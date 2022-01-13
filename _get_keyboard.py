# 检查哪个键盘可以用
from interception import  *
from consts import *
from stroke import *
import time

class ScanCode():
    ESC = 1
    NUM1 = 2
    NUM2 = 3
    NUM3 = 4
    NUM4 = 5
    NUM5 = 6
    NUM6 = 7
    NUM7 = 8
    NUM8 = 9
    NUM9 = 10
    NUM0 = 11
    M = 50
    MINUS = 12

    KEY_DOWN = 0
    KEY_UP = 1

def send_key(device:int, scancode:int):
    c = interception()
    c.send(device, key_stroke(scancode,ScanCode.KEY_DOWN,0))
    c.send(device, key_stroke(scancode,ScanCode.KEY_UP,0))

if __name__ == "__main__":
    # time.sleep(5)
    for device in range(MAX_KEYBOARD):
        numkey = eval('ScanCode.NUM' + str(device))
        send_key(device, numkey)
    
    # 最终发送成功的设备会输出其数值