import sqlite3

CONN = None

def connect(file_name):
    global CONN
    CONN = sqlite3.connect(file_name)

def load_schema(schema_file):
    cur = CONN.cursor()
    script = open(schema_file).read()
    cur.executescript(script)
    CONN.commit()

class Person:

    def __init__(self, first_name, last_name, age):
        self.pk = None
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.pets = []

    def create(self):
        cur = CONN.cursor()
        cur.execute('insert into person(first_name, last_name, age) values (?,?,?)',
                    (self.first_name, self.last_name, self.age))
        self.pk = cur.lastrowid
        CONN.commit()

    def update(self):
        cur = CONN.cursor()
        cur.execute('update person set first_name=?, last_name=?, age=? where id=?',
                    (self.first_name, self.last_name, self.age, self.pk))
        CONN.commit()

    def delete(self):
        cur = CONN.cursor()
        cur.execute('delete from person where id=?', (self.pk,))
        CONN.commit()

    @classmethod
    def read(self, pk):
        cur = CONN.cursor()
        cur.execute('select id, first_name, last_name, age from person where id=?', (pk,))
        row = cur.fetchone()
        obj = Person(*row[1:])
        obj.pk = row[0]
        return obj



class Pet:
    
    def __init__(self, name, breed, age, dead):
        self.pk = None
        self.name = name
        self.breed = breed
        self.age = age
        self.dead = dead
        self.owners = []

    def create(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def read(self, pk):
        pass
