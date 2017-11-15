class Person(object):

    def __init__(self, first_name, 
                 last_name, age, pets):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.pets = pets

class Pet(object):
    def __init__(self, name, breed, 
                 age, dead):
        self.name = name
        self.breed = breed
        self.age = age
        self.dead = dead
        self.owners = []

# simulate insert
fluffy = Pet('Fluffy', 'Unicorn', 12, False)
gigantor = Pet('Gigantor', 'Robot', 2, False)
pete = Person("Zed", "Shaw", 43, [fluffy, gigantor])
fluffy.owners.append(pete)
gigantor.owners.append(pete)

DB = {
    'person': [ pete ],
    'pet': [fluffy, gigantor],
}

dead_pets = [pet for pet in DB['pet'] if pet.dead == False]
print(dead_pets)


