# make an example class
import random



class Character:
    def __init__(self, name, health, isDead, strength):
        self.name = name
        self.health = random.randint(90, 110)
        self.isDead = isDead
        self.strength = random.randint(5, 10)
    def greet(self):
        if self.isDead:
            print(f"Hello, my name is {self.name} and I am dead!")
        else:
            print(f"Hello, my name is {self.name} and I am not dead!")
    def instigate(self, person):
        if self.isDead:
            print(f"{self.name} is dead and cannot instigate {person}")
        else:
            print(f"I am {self.name} and I am going to punch {person}")
            person.isDead = True
    def attack(self, opponent):
        damage = random.randint(10, 13)
        opponent.health -= damage
        print(f"{self.name} hit {opponent.name}! {opponent.name} lost {damage} health! {opponent.name} has {opponent.health} health")
    def heathCheck(self):
        if self.health <= 0:
            self.isDead = True


character1 = Character('Bob', 100, True, 15)
character2 = Character('Steve', 100, True, 20)

while 7 == 7:
    user_input = input('do you hit bob? y/n')
    if user_input == 'y':
        character2.attack(character1)
    elif user_input == 'n':
        print('bob will hit you now')
        character1.attack(character2)

    if character1.health <= 0:
        print('bob is dead')
        break
    elif character2.health <= 0:
        print('steve is dead')
        break



