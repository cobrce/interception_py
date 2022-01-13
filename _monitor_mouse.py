from interception import  *
from consts import *

if __name__ == "__main__":
    c = interception()
    c.set_filter(interception.is_mouse,interception_filter_mouse_state.INTERCEPTION_FILTER_MOUSE_ALL.value)
    # c.set_filter(interception.is_mouse,interception_filter_mouse_state.INTERCEPTION_FILTER_MOUSE_WHEEL.value)
    while True:
        device = c.wait()
        print('Device: %d' % device)
        stroke = c.receive(device)
        if type(stroke) is mouse_stroke:
            print("state: %d,\tflags: %d,\trolling: %d,\tx: %d,\ty: %d,\tinfo:%d" % (stroke.state, stroke.flags, stroke.rolling, stroke.x, stroke.y, stroke.information))
        c.send(device,stroke)
        # hwid = c.get_HWID(device)
        # print(u"%s" % hwid)
