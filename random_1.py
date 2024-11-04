import random
import time
class LCG:
    def __init__(self, seed):
        self.seed = seed
        self.modulus = 2**31 - 1
        self.multiplier = 48271
        self.increment = 0
    
    def random(self):
        self.seed *= self.multiplier
        self.seed += self.increment
        self.seed %= self.modulus
        return self.seed


lcg = LCG((time.time() - int(time.time())) * 10)

for i in range(10):
    print(random.randint(0, 1))

