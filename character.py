# make an example class
class Character:
    def __init__(self, name, health, isDead, strength):
        self.name = name
        self.health = health
        self.isDead = isDead
        self.strength = strength
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
        opponent.health -= self.strength
        print(f"{self.name} hit {opponent.name}! {opponent.name} lost {self.strength} health! {opponent.name} has {opponent.health} health")


character1 = Character('Bob', 100, True, 15)
character2 = Character('Steve', 100, True, 20)


character1.attack(character2)
