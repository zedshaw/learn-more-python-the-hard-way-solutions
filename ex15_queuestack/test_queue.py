from queue import *

def test_shift():
    colors = Queue()
    colors.shift("Pthalo Blue")
    assert colors.count() == 1
    colors.shift("Ultramarine Blue")
    assert colors.count() == 2

def test_unshift():
    colors = Queue()
    colors.shift("Magenta")
    colors.shift("Alizarin")
    assert colors.unshift() == "Magenta"
    assert colors.unshift() == "Alizarin"
    assert colors.unshift() == None

def test_first():
    colors = Queue()
    colors.shift("Cadmium Red Light")
    assert colors.first() == "Cadmium Red Light"
    colors.shift("Hansa Yellow")
    assert colors.first() == "Cadmium Red Light"
    colors.shift("Pthalo Green")
    assert colors.first() == "Cadmium Red Light"

def test_drop():
    colors = Queue()
    colors.shift("Cad Red")
    colors.shift("Hansa Yellow")
    assert colors.count() == 2
    colors.drop()
    assert colors.count() == 1
    assert colors.first() == "Cad Red"
    colors.drop()
    assert colors.first() == None
