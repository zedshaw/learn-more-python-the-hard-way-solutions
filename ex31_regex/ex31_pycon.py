>>> import re
>>> m = re.match(r".*BC?$", "helloB").span()
>>> re.match(r".*BC?$", "helloB").span()
(0, 6)
>>> re.match(r"[A-Za-z][0-9]+", "A1232344").span()
(0, 8)
>>> re.match(r"[A-Za-z][0-9]+", "abc1234").span()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'span'
>>> re.match(r"[A-Za-z][0-9]+", "1234").span()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'span'
>>> re.match(r"[A-Za-z][0-9]+", "b493034").span()
(0, 7)
>>> 
