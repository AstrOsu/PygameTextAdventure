import random, time
from getpass import getpass

standard_1 = {
    "STR": 5,
    "DEF": 6,
    "MGK": 0.001,
    "SPD": 0.2,
    "LCK": 0.02
}


class Character:
    def __init__(self):
        self.stats = {
            "STR": 0,
            "DEF": 0,
            "MGK": 0,
            "SPD": 0,
            "VIT": 100
        }
        self.points = 100
        self.set_name()
        self.set_stats()

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