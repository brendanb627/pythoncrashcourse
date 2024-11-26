# go through existing todos, listing each one asking user if they completed it
# If they completed it, remove it from the list, if not keep it
# ask user to add more todos
#Allow them to quit out when they are done adding their todos.
import re

def read_list():
    todo_list = ''
    f = open("todos.txt", "r")
    todos = f.read().split("\n")
    for i in range(len(todos)):
        todo_list += (f"{i} {todos[i]}\n")
    return todo_list

def add_to_list(item):
    f = open("todos.txt", "a")
    f.write(item + "\n")
    f.close()

def remove_from_list(num):
    delims = "\n"
    f = open("todos.txt", "r")
    content = re.split(delims, f.read())
    if int(num) <= len(content) - 1:
        content.pop(int(num))
        f = open("todos.txt", "w")
        f.write("\n".join(content))
        f.close()
        return "item removed"
    else:
        return "Invalid number"

running = True

while running:
    print(read_list())
    user_input = input('press the number to remove item. write "add" then the item to add to the list ')
    if user_input[0] == 'a' and user_input[1] == 'd' and user_input[2] == 'd':
        add_to_list(user_input[4:])
    elif user_input.isdigit():
        print(remove_from_list(user_input))




