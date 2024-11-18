def factorial(x):
    #base case
    if x <= 1:
        return 1
    #recursive case
    else:
        return x * factorial(x-1)
    

def fibonacci(x):
    if x <= 1:
        return x
    else:
        return fibonacci(x - 1) + fibonacci(x - 2)
    

def prepareString(string):
    output_string = ""
    for c in string:
        if c.isalpha():
            output_string += c.lower()
    return output_string


def isPalindrome(rawInput):
    input = prepareString(rawInput)
    if len(input) <= 1:
        return True
    else:
        if input[0] == input[-1]:
            return isPalindrome(input[1:-1])
        else:
            return False
        
print(isPalindrome(prepareString('Mom')))

def hanoiSolver(start, end, helper, disks):
    if disks <= 0:
        return
    else:
        hanoiSolver(start, helper, end, disks - 1)
        print(f"Move disk from {start} to {end}")
        hanoiSolver(helper, end, start, disks - 1)



hanoiSolver("A", "C", "B", 3)






#print(fibonacci(5))
   
for i in range(1, 11):
    #print(f"{i}! = {factorial(i)}")
    pass
