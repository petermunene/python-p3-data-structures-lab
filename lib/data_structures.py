spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    food_name=[]
    for spicy_food in spicy_foods:
        name=spicy_food["name"]
        food_name.append(name)
    return food_name
    pass

def get_spiciest_foods(spicy_foods):
    spicy_levels=[]
    for spicy_food in spicy_foods:
        heat_level=spicy_food["heat_level"]
        if heat_level > 5:
            spicy_levels.append(spicy_food)
    return spicy_levels
    pass

def print_spicy_foods(spicy_foods):
    for spicy_food in spicy_foods:
        name = spicy_food['name']
        country = spicy_food['cuisine']
        heat_level = spicy_food['heat_level']
        print(f"{name} ({country}) | Heat Level: {'🌶' * heat_level}")
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for spicy_food in spicy_foods:
        if spicy_food["cuisine"]==cuisine:
            return spicy_food
    pass

def print_spiciest_foods(spicy_foods):
    for spicy_food in spicy_foods:
        if spicy_food["heat_level"] > 5:
            name = spicy_food['name']
            country = spicy_food['cuisine']
            heat_level = spicy_food['heat_level']
            print(f"{name} ({country}) | Heat Level: {'🌶' * heat_level}")
    pass

def get_average_heat_level(spicy_foods):
    total=[]
    for spicy_food in spicy_foods :
        heat_level=spicy_food["heat_level"]
        total.append(heat_level)
    average=sum(total)/len(spicy_foods)
    return average
    pass

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    pass
