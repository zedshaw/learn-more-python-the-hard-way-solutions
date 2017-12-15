from ed import ed
import os

def test_process():
    buffer = ed.Buffer()
    buffer.append('Test')
    buffer.append('Test')
    ed.process(",p", buffer)
    ed.process(",n", buffer)
    ed.process("1p", buffer)
    ed.process("1,2p", buffer)
    ed.process('f tests/out.txt', buffer)
    ed.process("w", buffer)

