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

def test_change():
    b = Buffer()

def test_delete():
    b = Buffer()

def test_edit():
    b = Buffer()
    base_file = "tests/test_buffer.py"
    b.edit(base_file)
    expected = [x.rstrip() for x in open(base_file).readlines()]
    assert b.lines == expected
    assert b.file_name == base_file

def test_file():
    b = Buffer()
    base_file = "tests/test_buffer.py"
    b.file(base_file)
    assert b.file_name == base_file

def test_glob():
    b = Buffer()

def test_insert():
    b = Buffer()

def test_join():
    b = Buffer()

def test_mark():
    b = Buffer()

def test_move():
    b = Buffer()

def test_nprint():
    b = Buffer()
    b.nprint(0,0)

def test_print():
    b = Buffer()
    b.print(0,0)

def test_read():
    b = Buffer()

def test_subst():
    b = Buffer()

def test_write():
    b = Buffer()
    b.file("tests/out.txt")
    b.write()
    assert os.path.exists("tests/out.txt")

