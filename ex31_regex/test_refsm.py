import refsm


def test_match():
    assert refsm.match('A990099')
    assert refsm.match('d9848')
    assert refsm.match('Z99%#$') == False
    assert refsm.match('%6666') == False
    assert refsm.match('A#$#') == False
    assert refsm.match('AZZZZ') == False

def test_ReFSM():

    fsm = refsm.ReFSM()
    fsm.handle('%')
    fsm.handle('%')
    assert fsm.state_name == 'INVALID'
