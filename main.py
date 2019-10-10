import sys
import math
import random

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

class Ship:
    def __init__(self,x,y, speed, owned, stock, orientation):
        self.x = x
        self.y = y
        self.speed = speed
        self.owned = owned
        self.stock = stock
        self.orientation = orientation

    def closestShip(self,ships):
        distance = 9999
        closest_ship = None
        for ship in ships:
            temp_distance = self.manhattanDistance(ship)
            if temp_distance < distance:
                distance = temp_distance
                closest_ship = ship
        return closest_ship

    def manhattanDistance(self,entity):
        return abs(entity.x - self.x) + abs(entity.y - self.y)

    def closestBarrel(self,barrels):
        distance = 9999
        closest_barrel = None
        for barrel in barrels:
            temp_distance = self.manhattanDistance(barrel)
            if temp_distance < distance:
                distance = temp_distance
                closest_barrel = barrel
        if distance > 10:
            closest_barrel = None
        return closest_barrel

    def closestMine(self,mines):
        distance = 9999
        closest_mine = None
        for mine in mines:
            temp_distance = self.manhattanDistance(mine)
            if temp_distance < distance:
                distance = temp_distance
                closest_mine = mine
        if distance > 10:
            closest_mine = None
        return closest_mine


class Barrel:
    def __init__(self,x,y,amount):
        self.x = x
        self.y = y
        self.amount = amount

class Mine:
    def __init__(self,x,y):
        self.x = x
        self.y = y

# game loop
while True:
    my_ships = []
    their_ships = []
    barrels = []
    mines = []
    my_ship_count = int(input())  # the number of remaining ships
    entity_count = int(input())  # the number of entities (e.g. ships, mines or cannonballs)
    for i in range(entity_count):
        entity_id, entity_type, x, y, arg_1, arg_2, arg_3, arg_4 = input().split()
        entity_id = int(entity_id)
        x = int(x)
        y = int(y)
        arg_1 = int(arg_1)
        arg_2 = int(arg_2)
        arg_3 = int(arg_3)
        arg_4 = int(arg_4)
        if(entity_type == "SHIP"):
            if(arg_4 == 1):
                my_ships.append(Ship(x,y,arg_2,True,arg_3,arg_1))
            else:
                their_ships.append(Ship(x,y,arg_2,True,arg_3,arg_1))
        elif(entity_type == "BARREL"):
            barrels.append(Barrel(x,y,arg_1))
        elif(entity_type == "MINE"):
            mines.append(Mine(x,y))

    for i in range(my_ship_count):
        closest_mine = my_ships[i].closestMine(mines)
        closest_ship = my_ships[i].closestShip(their_ships)
        closest_barrel = my_ships[i].closestBarrel(barrels)

        if(random.randint(0,4) != 0) and closest_barrel != None:
            print("MOVE " + str(closest_barrel.x)+ " " + str(closest_barrel.y))
        elif closest_mine != None and random.randint(0,4) == 0:
            print("FIRE " + str(closest_mine.x)+ " " + str(closest_mine.y))
        elif closest_ship != None:
            print("FIRE " + str(closest_ship.x)+ " " + str(closest_ship.y))
        else:
            print("MOVE " + str(random.randint(0,22)) + " " + str(random.randint(0,20)))
