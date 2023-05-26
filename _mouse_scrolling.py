from interception import *
from win32api import GetSystemMetrics

mouse = 13
x,y = 100, 290

screen_width = GetSystemMetrics(0)
screen_height = GetSystemMetrics(1)
xT = int((0xFFFF * x) / screen_width)
yT = int((0xFFFF * y) / screen_height)

context = interception()
mstroke = mouse_stroke(interception_mouse_state.INTERCEPTION_MOUSE_WHEEL.value,
                           interception_mouse_flag.INTERCEPTION_MOUSE_MOVE_ABSOLUTE.value,
                           120,
                           xT,
                           yT,
                           0)

context.send(mouse,mstroke) # we send the key stroke, now the right button is down

# mstroke.state = interception_mouse_state.INTERCEPTION_MOUSE_LEFT_BUTTON_UP.value # update the stroke to release the button
# mstroke.state = interception_mouse_state.INTERCEPTION_MOUSE_RIGHT_BUTTON_UP.value # update the stroke to release the button
# context.send(mouse,mstroke) #button right is up
# %%
