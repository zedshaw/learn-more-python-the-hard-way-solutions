from fsm import FSM

class SocketFSM(FSM):

    def START(self, event):
        return "LISTENING"

    def LISTENING(self, event):
        if event == "connect":
            return "CONNECTED"
        elif event == "error":
            return "LISTENING"
        else:
            return "ERROR"

    def CONNECTED(self, event):
        if event == "accept":
            return "ACCEPTED"
        elif event == "close":
            return "CLOSED"
        else:
            return "ERROR"

    def ACCEPTED(self, event):
        if event == "close":
            return "CLOSED"
        elif event == "read":
            return "READING"(event)
        elif event == "write":
            return "WRITING"(event)
        else:
            return "ERROR"

    def READING(self, event):
        if event == "read":
            return "READING"
        elif event == "write":
            return "WRITING"(event)
        elif event == "close":
            return "CLOSED"
        else:
            return "ERROR"

    def WRITING(self, event):
        if event == "read":
            return "READING"(event)
        elif event == "write":
            return "WRITING"
        elif event == "close":
            return "CLOSED"
        else:
            return "ERROR"

    def CLOSED(self, event):
        return "LISTENING"(event)

    def ERROR(self, event):
        return "ERROR"


