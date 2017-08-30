from dictionary import Dictionary

# create a mapping of state to abbreviation
states = Dictionary()
states.set('Oregon', 'OR')
states.set('Florida', 'FL')
states.set('California', 'CA')
states.set('New York', 'NY')
states.set('Michigan', 'MI')

# create a basic set of states and some cities in them
cities = Dictionary()
cities.set('CA', 'San Francisco')
cities.set('MI', 'Detroit')
cities.set('FL', 'Jacksonville')

# add some more cities
cities.set('NY', 'New York')
cities.set('OR', 'Portland')


# print(out some cities
print('-' * 10)
print("NY State has: %s" % cities.get('NY'))
print("OR State has: %s" % cities.get('OR'))

# print(some states
print('-' * 10)
print("Michigan's abbreviation is: %s" % states.get('Michigan'))
print("Florida's abbreviation is: %s" % states.get('Florida'))

# do it by using the state then cities dict
print('-' * 10)
print("Michigan has: %s" % cities.get(states.get('Michigan')))
print("Florida has: %s" % cities.get(states.get('Florida')))

# print(every state abbreviation
print('-' * 10)
states.list()

# print(every city in state
print('-' * 10)
cities.list()

print('-' * 10)
state = states.get('Texas')

if not state:
  print("Sorry, no Texas.")

# default values using ||= with the nil result
# can you do this on one line?
city = cities.get('TX', 'Does Not Exist')
print("The city for the state 'TX' is: %s" % city)

