#%%
import time
from interception import *
from win32api import GetSystemMetrics

#%%
# 需要点击的坐标
x, y = 32, 32
screen_width = GetSystemMetrics(0)
screen_height = GetSystemMetrics(1)

# create a context for interception to use to send strokes, in this case
# we won't use filters, we will manually search for the first found mouse
context = interception()

# loop through all devices and check if they correspond to a mouse
mouseList = []
for mouse in range(MAX_DEVICES):
    if interception.is_mouse(mouse):
        mouseList.append(mouse)

# no mouse we quit
if (len(mouseList) == 0):
    print("No mouse found")
    exit(0)

# 通过点击检查哪些鼠标可以用
for mouse in mouseList:
    print("Mouse: %d" % mouse)

    mstroke = mouse_stroke(interception_mouse_state.INTERCEPTION_MOUSE_LEFT_BUTTON_DOWN.value,
                            interception_mouse_flag.INTERCEPTION_MOUSE_MOVE_ABSOLUTE.value,
                            0,
                            int((0xFFFF * x) / screen_width),
                            int((0xFFFF * y) / screen_height),
                            0)

    context.send(mouse,mstroke)

    mstroke.state = interception_mouse_state.INTERCEPTION_MOUSE_LEFT_BUTTON_UP.value
    context.send(mouse,mstroke)
    time.sleep(2)
# %%
