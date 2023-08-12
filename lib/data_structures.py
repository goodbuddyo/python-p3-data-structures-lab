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


# get_names() that takes a list of spicy_foods 
# # and returns a list of strings with the names of each spicy food.
def get_names(spicy_foods):
    spicy_list = []
    for i in spicy_foods:
        spicy_list.append(i['name'])
    # print(spicy_list)
    return spicy_list

# get_names(spicy_foods)

# takes a list of spicy_foods 
# returns a list of dictionaries where the heat level of the food is greater than 5.


def get_spiciest_foods(spicy_foods):
    hot_stuff = []
    for i in spicy_foods:
        if i['heat_level'] >= 5:
            hot_stuff.append(i)
    # print(hot_stuff)
    return hot_stuff

    # print(i)
    # {'name': 'Green Curry', 'cuisine': 'Thai', 'heat_level': 9}
    # {'name': 'Buffalo Wings', 'cuisine': 'American', 'heat_level': 3}
    # {'name': 'Mapo Tofu', 'cuisine': 'Sichuan', 'heat_level': 6}

# get_spiciest_foods(spicy_foods)

# output to the terminal each spicy food in the following format using print(): 
# Buffalo Wings (American) | Heat Level: 🌶🌶🌶


def print_spicy_foods(spicy_foods):
    for i in spicy_foods:
        heatcount = int(i['heat_level'])
        print(i['name'], '(', end='')
        print(i['cuisine'], end='')
        print(') | Heat Level: ', end='')
        # for h in range(heatcount):
        #    print('🌶', end='')
        print('🌶'*heatcount, end='')
        print('', end='\n')


# print_spicy_foods(spicy_foods)

#  takes a list of spicy_foods and a string representing a cuisine,
# and returns a single dictionary for the spicy food whose cuisine matches the cuisine string passed in.
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for i in spicy_foods:
        my_cuisine = i['cuisine']
        if my_cuisine == cuisine:
            print(i)
            return i

# get_spicy_food_by_cuisine(spicy_foods, 'Thai')

# takes a list of spicy_foods and outputs to the terminal 
# ONLY the spicy foods that have a heat level greater than 5, in the following format:
# Buffalo Wings (American) | Heat Level: 🌶🌶🌶.


def print_spiciest_foods(spicy_foods):
    my_spicy_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(my_spicy_foods)

    # for i in spicy_foods:
    #    if i['heat_level'] >= 5:
    #        heatcount = int(i['heat_level'])
    #        print(i['name'], '(', end='')
    #        print(i['cuisine'], end='')
    #        print(') | Heat Level: ', end='')
    #        print('🌶'*heatcount, end='')
    #        print('', end='\n')

# print_spiciest_foods(spicy_foods)


# Define a function average_heat_level() that takes a list of spicy_foods 
# and returns an integer representing the average heat level of all the spicy foods in the array.

def average_heat_level(spicy_foods):
    num = 0
    total = 0
    avg = 0.0
    for i in spicy_foods:
        num = num + 1
        total = total + int(i['heat_level'])
        avg = float(total/num)
    # print('num = ', num)
    # print('total = ', total)
    print('avg = ', avg)
    return avg


def get_average_heat_level(spicy_foods):
    return average_heat_level(spicy_foods)


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    print(spicy_foods)
    return spicy_foods


# create_spicy_food(
#    spicy_foods,
#    {
#        'name': 'Griot',
#        'cuisine': 'Haitian',
#        'heat_level': 10,
#    }
# )
