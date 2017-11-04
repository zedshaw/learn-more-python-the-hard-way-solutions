from unittest.mock import patch
import sh


@patch('subprocess.run')
def test_basic(sub_run):
    result = sh.run('ls -l')
    assert sub_run.called

def test_parse():
    result = sh.parse('ls -l')
    assert result == ['ls', '-l']

    result = sh.parse('')
    assert result == []

    result = sh.parse('     ')
    assert result == []

@patch('sys.exit')
@patch('os.chdir')
@patch('subprocess.run')
def test_interpret(sub_run, chdir, sys_exit):
    result = sh.interpret(['exit'])
    assert sys_exit.called

    result = sh.interpret(['cd', '..'])
    assert chdir.called

    result = sh.interpret(['ls', '-l'])
    assert sub_run.called


@patch('subprocess.run')
def test_empty_input(sub_run):
    result = sh.run('')
    assert not sub_run.called
