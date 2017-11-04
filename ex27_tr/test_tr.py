import tr

def test_translate():
    test_input = "ttyyhhxxaa"
    results = tr.translate('t', 'X', test_input)
    assert results == "XXyyhhxxaa"

def test_tr_basic():
    results = tr.main(['t', 'X'], 'ttyyhhxxaa')
    assert results == "XXyyhhxxaa"

    results = tr.main(['XX', 'tt'], results)
    assert results == 'ttyyhhxxaa'

    results = tr.main(['hh', 'XX'], results)
    assert results == 'ttyyXXxxaa'

    results = tr.main(['hh', 'XX'], '')
    assert results == ''

def test_tr_truncate():
    results = tr.main(['-t', 'httttt', 'Xx'], 'httttttaaaaa')
    assert results == 'Xxtttttaaaaa'



