import sys
import diff
import io

def run_diff(style):
    out = io.StringIO()
    diff.main(style, 'diff.py', 'sample.py', out)
    # should probably do a better test 
    return out.getvalue()


def test_basic():
    result = run_diff('u')
    assert result

    result = run_diff('c')
    assert result

    result = run_diff('n')
    assert result

