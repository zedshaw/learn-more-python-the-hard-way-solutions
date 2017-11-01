>>> magic = "abracadabra"
>>> magic_sa = []
>>> for i in range(0, len(magic)):
...     magic_sa.append(magic[i:])
... 
>>> magic_sa
['abracadabra', 'bracadabra', 'racadabra', 'acadabra',
 'cadabra', 'adabra', 'dabra', 'abra', 'bra', 'ra', 'a']
>>> magic_sa = sorted(magic_sa)
>>> magic_sa
['a', 'abra', 'abracadabra', 'acadabra', 'adabra', 'bra',
 'bracadabra', 'cadabra', 'dabra', 'ra', 'racadabra']
>>> 
