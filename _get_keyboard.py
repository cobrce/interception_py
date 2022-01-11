# 此脚本返回 0 - 9 的所有数值, 似乎无法正确判断keyboard

from interception import *

context = interception()

for i in range(10):
    if interception.is_keyboard(i):
        print('keyboard:',i)
