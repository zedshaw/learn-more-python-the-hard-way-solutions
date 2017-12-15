from simple_orm import *
import os

if os.path.exists('data.db'): os.remove('data.db')
connect(':memory:')
load_schema('02_create.sql')

def test_Person():
    joe = Person('Joe', 'Franks', 35)
    mary = Person('Mary', 'Abeline', 25)
    joe.create()
    mary.create()
    joe.first_name = 'Alex'
    joe.update()
    joe2 = Person.read(joe.pk)
    assert joe2.first_name == 'Alex'
    joe2.delete()
    

