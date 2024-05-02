import random, time
from getpass import getpass

def get_stat_dict(STR, DEF, LCK, SPD, VIT):
    return {
        "STR": STR,
        "DEF": DEF,
        "LCK": LCK,
        "SPD": SPD,
        "VIT": VIT
    }


class Character:
    def __init__(self, name = "", stats = {}):
        if len(stats) == 0:
            self.stats = get_stat_dict(0, 0, 0, 0, 100)
        else:
            self.stats = stats
        
        if name == "":
            self.points = 100
            self.set_name()
            self.set_stats()
        else:
            self.name = name
            self.points = 0
    
    def set_name(self):
        print("What would you like your name to be?")
        self.name = input("> ")

    def set_stats(self):
        while self.points > 0:
            print("Select a stat to upgrade: [STR], [DEF], [LCK], [SPD], or [VIT]")
            stat_upgrade = input("> ")
            if stat_upgrade in self.stats.keys():
                print(f"\nEnter a number of points to input into that stat. You have {self.points} points remaining.")
                try:
                    point_count = int(input("> "))
                    if point_count > 0 and point_count <= self.points:
                        self.stats[stat_upgrade] += point_count
                        self.print_stats()
                        self.points -= point_count
                    else:
                        print("Invalid number entered. Please try again.")
                    print("")
                except ValueError:
                    print("Invalid number or not a number. Try rounding to the nearest whole number.")
            else:
                print("Invalid choice. Try CAPITALIZING the characters and/or removing brackets.")

    # dev functions
    def print_name(self):
        print("NAME: " + str(self.name))

    def print_stats(self):
        print("STR: " + str(self.stats["STR"]))
        print("DEF: " + str(self.stats["DEF"]))
        print("LCK: " + str(self.stats["LCK"]))
        print("SPD: " + str(self.stats["SPD"]))
        print("VIT: " + str(self.stats["VIT"]))

    def attack(self, target):
        damage = self.stats["STR"] - target.stats["DEF"]

        if damage > 0:
            target.stats["VIT"] -= damage
            return damage
        else:
            target.stats["VIT"] -= 1
            return 1



"""

STR is attack damage
DEF is defense

Damage is calculated as STR - DEF
If defense is equal to or higher than STR, set damage to 1

LCK adds a random number from -[value given / 5] to [value given / 5] to ALL OTHER STATS
SPD is probability of dodging an attack
50 SPD = 25% chance of dodging the attack
VIT = health

"""

"""
SWORD: DEFEATS SHIELD
BOW: DEFEATS SWORD
SHIELD: DEFEATS BOW AND APPLIES ENRAGED TO OPPONENT

"""