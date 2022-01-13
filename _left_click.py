#%%
from interception import *
from win32api import GetSystemMetrics
#%%
# 需要点击的坐标
# x,y = 553,337
x,y = 23,303
# x,y = 554,82
# get screen size
screen_width = GetSystemMetrics(0)
screen_height = GetSystemMetrics(1)

# create a context for interception to use to send strokes, in this case
# we won't use filters, we will manually search for the first found mouse
context = interception()

# loop through all devices and check if they correspond to a mouse
mouse = 0
for i in range(MAX_DEVICES):
    if interception.is_mouse(i):
        mouse = i
        break

# no mouse we quit
if (mouse == 0):
    print("No mouse found")
    exit(0)

# 鼠标14可以用
mouse = 11

# we create a new mouse stroke, initially we use set right button down, we also use absolute move,
# and for the coordinate (x and y) we use center screen
mstroke = mouse_stroke(interception_mouse_state.INTERCEPTION_MOUSE_LEFT_BUTTON_DOWN.value,
                           interception_mouse_flag.INTERCEPTION_MOUSE_MOVE_ABSOLUTE.value,
                           0,
                           int((0xFFFF * x) / screen_width),
                           int((0xFFFF * y) / screen_height),
                           0)

context.send(mouse,mstroke) # we send the key stroke, now the right button is down

mstroke.state = interception_mouse_state.INTERCEPTION_MOUSE_LEFT_BUTTON_UP.value # update the stroke to release the button
# mstroke.state = interception_mouse_state.INTERCEPTION_MOUSE_RIGHT_BUTTON_UP.value # update the stroke to release the button
context.send(mouse,mstroke) #button right is up
# %%
