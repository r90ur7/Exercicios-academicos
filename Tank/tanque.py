from traceback import print_list
from unicodedata import name
from Tank import Tank
#a = Tank('bob')
#b = Tank('Claide')
my_tank = Tank('bob')

# print(my_tank.name, my_tank.armor)
# print(my_tank)
tanks = {"a" : Tank('Alice'), 'b': Tank('bob'), 'c' : Tank('carol')}

alive_tanks = len(tanks)

while alive_tanks > 1:
    for tank_name in sorted(tanks.keys()):
        print(tank_name, tanks[tank_name])
    first = input("who fires? " ).lower()
    second = input("who at " ).lower()
    try:
        # aqui ocorre as intanciações
     first_tank = tanks[first]
     second_tank = tanks[second]




    except KeyError:
        print("No,surch Tank", name)
        continue
    if not first_tank.alive or not second_tank.alive:
        print("One of  those is dead!")
    print("*"*30)
    first_tank.fire(second_tank)
    if not second_tank.alive:
        alive_tanks -= 1
    
    print("*"*30)

for tank in tanks.values():
    if tank.alive:
        print(tank_name, "is the winner")
        break