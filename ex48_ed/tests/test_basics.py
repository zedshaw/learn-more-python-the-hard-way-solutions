from ed import ed

def test_process():
    buffer = ed.Buffer()
    buffer.append('Test')
    buffer.append('Test')
    ed.process(",p", buffer)

