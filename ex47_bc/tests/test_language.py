from calc.run import run

def test_simple_function():
    run(open("test1.calc").readlines())

def test_simple_script():
    run(open("test2.calc").readlines())
