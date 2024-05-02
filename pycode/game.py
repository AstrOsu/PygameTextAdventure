import character
import random, time
class Game:
    def __init__(self):
        self.p1 = character.Character()
        self.p2 = character.Character()
    
    def play_game(self):
        print("Welcome to the game, user.\n")
        time.sleep(1)
        print("The innkeeper has asked you to kill a swarm of rats.")
        rat = character.Character("Rat", character.get_stat_dict(10, 20, 0, 40, 50))
        self.combat(rat) 
    


    def combat(self, enemy):
        turn_order = 0
        if enemy.stats["SPD"] > self.p1.stats["SPD"]:
            turn_order = 1
        while self.p1.stats["VIT"] > 0 and enemy.stats["VIT"] > 0:
            print("Your stats: ")
            self.p1.print_stats()
            print("Enemy's stats: ")
            enemy.print_stats()
            if turn_order % 2 == 0:
                print("What would you like to do?")
                choice = input("> ")
                if choice.lower() == "attack":
                    self.p1.attack(enemy)
                    turn_order += 1
            else:
                damage = enemy.attack(self.p1)
                print(f"{enemy.name} attacked you and dealt {damage} damage!")
