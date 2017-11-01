import subprocess
import hexdump



def test_compare_output():
    out = subprocess.run(["hexdump","test_hexdump.py"], check=True, stdout=subprocess.PIPE) 

def test_reshape():
    even = [1,2,3,4,5,6,7,8]
    expect = [[1, 2], [3, 4], [5, 6], [7, 8]]
    assert hexdump.reshape(even, 2) == expect

    even = [1,2,3,4,5,6,7,8]
    expect = [[1,2,3], [4,5,6], [7,8]]
    assert hexdump.reshape(even, 3) == expect

    odd = [1,2,3,4,5,6,7,8,9]
    expect = [[1,2], [3,4], [5, 6], [7,8], [9]]
    assert hexdump.reshape(odd, 2) == expect

    odd = [1,2,3,4,5,6,7,8,9]
    expect = [[1,2,3], [4,5,6], [7,8,9]]
    assert hexdump.reshape(odd, 3) == expect



