import Leap, sys, thread, time
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

class SampleListener(Leap.Listener):

    state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']
    run = True
    subpass = ''
    subpass_ = ''
    password = ''

    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"

        # Enable gestures
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
#        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
#        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
#        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print "Disconnected"

    def on_exit(self, controller):
        print "Exited"

    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
        frame = controller.frame()
        if self.run:
            # Get gestures
            #print'dhg'
            for gesture in frame.gestures():
                if gesture.type == Leap.Gesture.TYPE_CIRCLE:
                    circle = CircleGesture(gesture)
                    state = self.state_names[gesture.state]
                    # Determine clock direction using the angle between the pointable and the circle normal
                    if circle.pointable.direction.angle_to(circle.normal) <= Leap.PI/2:
                        clockwiseness = "clockwise"
                        if state is 'STATE_END':
                            print '%d' %int(circle.progress)
                            self.subpass += '%d' %int(circle.progress)
                            
                    else:
                        clockwiseness = "counterclockwise"
                        if state is 'STATE_END':
                            print '%d' %int(circle.progress)
                            self.subpass_ += '%d' %int(circle.progress)
            #print self.subpass
            if (frame.hands.is_empty and frame.gestures().is_empty and (self.subpass != '' or self.subpass_ != '')):
                self.password = self.subpass + self.subpass_
                print self.password
                self.run = False

    def state_string(self, state):
        if state == Leap.Gesture.STATE_START:
            return "STATE_START"

        if state == Leap.Gesture.STATE_UPDATE:
            return "STATE_UPDATE"

        if state == Leap.Gesture.STATE_STOP:
            return "STATE_STOP"

        if state == Leap.Gesture.STATE_INVALID:
            return "STATE_INVALID"

    def isDone(self):
        return not run

    def reset(self):
        self.run = True
        self.password = ''
        self.subpass = ''
        self.subpass_ = ''

def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()
