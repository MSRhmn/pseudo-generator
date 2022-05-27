from random import randint, choice

first_name = ['Alfred', 'Adrian', 'Ridley', 'Tom', 'Alfonso', 'Bennett', 'Sidney', 'Mike', 'George', 'Quintin', 'Steven', 'Martin', 'Spike', 'Stanley', 'Tony', 'Danny', 'Joe']
last_name = ['Hitchcock', 'Lyne', 'Scott', 'Hooper', 'Cuarón', 'Miller', 'Lumet', 'Nichols', 'Spielberg', 'Lucas', 'Tarantino', 'Scorecesse', 'Lee', 'Kubrick', 'Gilroy', 'Boyle', 'Wright']
street_names = ['Maple', 'Oak', 'Green', 'Bucketwheet', 'Mira', 'Chinatown', 'Park', 'Main', 'High', 'Montello', 'Bedford', 'Brunette', 'Helens', 'Glendale', 'Rufford', 'Curzon', 'Hillcrest']
cities = ['Las Vegas', 'California', 'New York City', 'Philadelphia', 'Bronx', 'San Jose', 'San Diego', 'San Antonio', 'Pittsburgh', 'Emerald City', 'Sin City', 'Tracy', 'Hayward', 'Greenville', 'Nashville', 'Kansas City', 'Oklahama City']
states = ['AZ', 'AK', 'NY', 'MT', 'MA', 'NV', 'CA', 'WA', 'NE', 'IA', 'IN', 'OH', 'AR', 'AL', 'GA', 'FL', 'SC']

pseudo_data = ''

for num in range(100):
  first = choice(first_name)
  last = choice(last_name)
  phone = f'{randint(100, 999)}-555-{randint(1000, 9999)}'
  street_num = randint(100, 999)
  street = choice(street_names)
  city = choice(cities)
  state = choice(states)
  zip = randint(10000, 99999)
  address = f'{street_num} {street} St, {city} {state} {zip}'
  email = f'{first.lower()}{last.lower()}@pseudomail.com'
  data = f'{first} {last}\n{phone}\n{address}\n{email}\n'
  pseudo_data += f'{data}\n'

with open('./data/generated_data.txt', 'w') as f:
  f_data = f.write(pseudo_data)
