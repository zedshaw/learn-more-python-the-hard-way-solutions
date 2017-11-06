from fsm import FSM


def match(what):
    """Will use an FSM to match [A-Za-z][0-9]+"""
  
    fsm = ReFSM()

    for c in what:
        fsm.handle(c)
        # exit early on first bad match

        if fsm.state_name == "INVALID":
            return False


    return fsm.matched


class ReFSM(FSM):

    def START(self, event):

        if event.isalpha():
            self.matched = False
            return "DIGITS"
        else:
            self.matched = False
            return "INVALID"

    def DIGITS(self, event):
        if event.isdigit():
            self.matched = True
            return "DIGITS"
        else:
            self.matched = False
            return "INVALID"

    def INVALID(self, event):
        self.matched = False
        return "INVALID"


