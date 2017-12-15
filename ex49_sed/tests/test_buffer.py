from ed.ed import Buffer
import os

def test_append():
    b = Buffer()
    b.append("This is a test.")
    assert b.lines[0] == "This is a test."
    b.append("a", address=0)
    assert b.lines[0] == "a"
    b.append("1", 1)
    assert b.lines[1] == "1"

def test_edit():
    b = Buffer()
    base_file = "tests/test_buffer.py"
    b.edit(base_file)
    assert b.lines == open(base_file).readlines()
    assert b.file_name == base_file

def test_file():
    b = Buffer()
    base_file = "tests/test_buffer.py"
    b.file(base_file)
    assert b.file_name == base_file

def test_nprint():
    b = Buffer()
    b.nprint(0,0)

def test_print():
    b = Buffer()
    b.print(0,0)

def test_write():
    b = Buffer()
    b.file("tests/out.txt")
    b.write()
    assert os.path.exists("tests/out.txt")

