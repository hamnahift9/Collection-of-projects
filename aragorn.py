import random
import sys

prize_list = ["Coin", "Hairpin", "Enchiridion", "Table", "Gold (5)"]

class Character:
    
    def __init__(self, name, alliance, max_health = 100):
        self.alliance = alliance
        self.max_health = max_health
        self.inventory = ["Potion"]
        self.weapon = [{'name' : "Sword", 'durability' : 100, 'state': "fine"}]
        self.health = max_health
        self.pick_up_availability = []
        self.progress = 0
        self.kill_count = 0
        self.restarts = 0
        
    def get_inventory(self):
        return self.inventory
    
    def get_alliance(self):
        return self.alliance
    
    def get_health(self):
        return self.health
    
    def get_max_health(self):
        return self.max_health
    
    def shift_alliance(self):
        if self.alliance == "Good":
            self.alliance = "Evil"
        else:
            self.alliance = "Good"
        print("Shifted alliance to", str(self.alliance) + "!")
        
    # Not using but keeping it in anyways
    def pick_up(self, item):
        if item in self.pick_up_availability:
            self.inventory.append(item)
            self.pick_up_availability.pop(self.pick_up_availability.index(item))
            print("Picked up", str(item) + "!")
        else:
            print("Could not find " + str(item) + ".")
        
    def hit(self):
        self.health -= 20
        print("Got hit! Health reduced by 20 points.")
        if self.health <= 0:
            print("Aragorn is dead :(")
            self.print_character()
            quit()
        
    def critical_hit(self):
        self.health -= 50
        print("Got hit critically! Health reduced by 50 points.")
        if self.health <= 0:
            print("Aragorn is dead :(")
            self.print_character()
            quit()
        
    def drop(self, item):
        if item in self.inventory:
            self.inventory.pop(self.inventory.index(item))
        else:
            print("Couldn't drop " + item + ".")
            
    def eat_bread(self, count = 1):
        for counter in range(count):
            if "Bread" in self.inventory:
                self.health += 50
                self.inventory.pop(self.inventory.index("Bread"))
                if self.health > self.max_health:
                    self.health = self.max_health
                print("Ate bread! Health is now", self.health, "points.")
            else:
                print("Couldn't eat bread.")
                
    def drink_potion(self, count = 1):
        for counter in range(count):
            if "Potion" in self.inventory:
                self.health = 100
                self.inventory.pop(self.inventory.index("Potion"))
                print("Drank a potion! Health is now 100 points.")
            else:
                print("Couldn't drink a potion.")

    def imp_choice(self):
        print("Aragorn is feeling particularly bad about himself when you come across a well filled with sparkling water.")
        choice = input("Drink from the water (y/n): ")
        if choice.lower() == "y":
            if self.restarts < 3:
                self.shift_alliance()
                self.kill_count = 0
                print("Aragorn feels like himself again. He wonders how long he can keep this up.")
            else:
                print("The water does not seem to have an effect anymore. Dejected, Aragorn jumps into the well.")
                quit()
        else:
            print("Aragorn is unsure on how to live with his actions. He jumps into the well.")
            quit()


    # returns fight outcomes- loss, win or escape.
    def fight_outcome(self, enemy):
        player_choice = input("Fight or Run: ")
        choice = player_choice.lower()
        chance = random.random()
        if choice == "fight" and self.weapon[0]['durability'] == "destroyed":
            print(f"You cannot fight. In wasting time trying to fight with your bare hands the {enemy} got the better of you.")
            return "loss"
        if enemy == "troll" and choice == "fight":
            if chance < 0.2:
                return "win"
            else:
                return "loss"
        elif enemy == "troll" and choice == "run": 
            if chance < 0.5:
                return "escape" 
            else:
                return "loss"
        if enemy == "bandit" and choice == "fight":
            if chance < 0.5:
                return "win"
            else:
                return "loss"
        elif enemy == "bandit" and choice == "run":
            if chance < 0.8:
                return "escape" 
            else:
                return "loss"
        return "loss"
    
    def win(self, enemy):
        print(f"You successfuly won the encounter! The {enemy} is dead.")
        self.kill_count += 1

        if random.random() < 0.5:
            self.weapon[0]['durability'] -= 10
            print("Your weapon feels a bit weaker.")
            if self.weapon[0]['durability'] == 0:
                self.weapon[0]['state'] = "destroyed"
                print("Your weapon is destroyed.")

        if random.random() < 0.5:
            index = random.randint(0, len(prize_list)-1)
            print(f"You found a {prize_list[index]}")
            user_choice = input("Pick up (y/n): ")
            if user_choice.lower() == "y":
                self.inventory.append(prize_list[index])
                print(f"Picked up {prize_list[index]}.")
                prize_list.pop(index)
            else:
                print(f"You left the item. Maybe it will keep the {enemy} guts company.")
            if len(prize_list) == 0:
                print("Congratulations! You have found the 5 items required to make Aragorn a hero.")
                quit()
        else:
            print(f"All you got were some {enemy} guts.")

        if self.kill_count >= 3:
            self.shift_alliance()
            print("\n")
            self.imp_choice()
    
    def escape(self,enemy):
        print(f"You escaped the {enemy}.")


    def take_input(self, input):
        input = input.lower()
        if input == "move":
            self.move()
        elif input == "eat":
            self.eat_bread()
        elif input == "drink":
            self.drink_potion()
        elif input == "pick up bread":
            self.pick_up("Bread")
        elif input == "pick up potion":
            self.pick_up("Potion")
        elif input == "status":
            Aragorn.print_character()
        elif input == "escape":
            quit()
        else:
            print("Couldn't recognize your input.")
    
    def print_character(self):
        print( "Alliance:", self.alliance )
        print( "Health:", self.health, "/", self.max_health )
        print( "Inventory:", self.inventory )
        print( "Progress:", self.progress )

    def move(self):
        self.pick_up_availability = []
        self.progress += 1
        encounter_random = random.random()
        interesting = False
        if encounter_random < 0.1:
            print("You came upon a giant troll.")
            troll_random = random.random()
            interesting = True
            outcome = self.fight_outcome("troll")
            if outcome == "loss":
                if troll_random < 0.8:
                    self.critical_hit()
                else:
                    self.hit()
            elif outcome == "win":
                self.win("troll")
            elif outcome == "escape":
                self.escape("troll")
        elif encounter_random < 0.4:
            print("You came upon a bandit.")
            bandit_random = random.random()
            interesting = True
            outcome = self.fight_outcome("bandit")
            if outcome == "loss":
                if bandit_random < 0.3:
                    self.critical_hit()
                else:
                    self.hit()
            elif outcome == "win":
                self.win("bandit")
            elif outcome == "escape":
                self.escape("bandit")
        bread_random = random.random()
        if bread_random < 0.3:
            interesting = True
            print("You found a loaf of bread lying on the ground.")
            self.pick_up_availability.append("Bread")
        potion_random = random.random()
        if potion_random < 0.1:
            interesting = True
            print("You found a potion hidden behind a bush! Wonder who left this lying around...")
            self.pick_up_availability.append("Potion")
            
        if not interesting:
            print("Nothing interesting happened :(")
            
Aragorn = Character("Aragorn", "Good")
Aragorn.take_input(input("What do you want to do? You can: \nmove, fight, run, \
pick something up (using Pick Up Bread or Pick Up Potion), \
eat, drink, get your status (using Status), or escape: "))
    
for i in range(10000):
    Aragorn.take_input(input("Next move: "))