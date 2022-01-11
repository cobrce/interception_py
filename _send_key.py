from interception import  *
from consts import *
from stroke import *
import time

class ScanCode():
    ESC = 1
    M = 50
    MINUS = 12

    KEY_DOWN = 0
    KEY_UP = 1

def send_key(device:int, scancode:int):
    c = interception()
    c.send(device, key_stroke(scancode,ScanCode.KEY_DOWN,0))
    c.send(device, key_stroke(scancode,ScanCode.KEY_UP,0))

if __name__ == "__main__":
    device = 8  # 0-10, 根据机器情况修改
    time.sleep(5)
    send_key(device, ScanCode.ESC)