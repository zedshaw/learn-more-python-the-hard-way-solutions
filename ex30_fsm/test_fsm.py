import fsm

def test_basic_connection():
    state = fsm.START()
    script = ["connect", "accept", "read", "read", "write", "close", "connect"]

    for event in script:
        print(event, ">>>", state)
        state = state(event)

