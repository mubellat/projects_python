import json
from functools import reduce

paste_json = open("aquarium.json", encoding="utf8")
data_aquarium = json.load(paste_json) # function to load dictionaries from json
animals = data_aquarium["data"]

def verify_fish(animal):
    if animal["type"] == "fish":
        return True
    return False

# animals_fish = list(filter(lambda animal: (animal["type"] == "fish"), animals)) 
# alternative way

animals_fish = list(filter(verify_fish, animals)) # applies the function to each element within the dictionary

def animal_name(animal):
    return animal["name"]

animal_fish_name = list(map(animal_name, animals_fish))
print(animal_fish_name)

def assign_to_tank(animals, names_selected, new_tank_number):
    def change_tank_number(animal):
        if animal["name"] in names_selected:
            animal["tank number"] = 42
        return animal
    return list(map(change_tank_number, animals))

new_aquarium = assign_to_tank(animals, animal_fish_name, 42)
print(new_aquarium)

def pick_animal_type(animal):
    return animal["type"], 1

def reducer(acc, val):  
    if val[0] not in acc.keys():
        acc[val[0]] = 0 + val[1]
    else:
        acc[val[0]] = acc[val[0]] + val[1]
    return acc

type_animals = list(map(pick_animal_type, animals))
print(type_animals)
animals_type_count = reducer(reducer, type_animals, {})
print(animals_type_count)