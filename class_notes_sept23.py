##hw how to read in from api
##1. put api in browser (can do print pretty), 2. find keys and save as key in code, 3. write code to get var
##naming conventions/code
# for dictionary in list
# for positiveIncrease_key in dictionary

#how to pull from file into list
#list comprehension
##print working directory
import os
os.system("pwd")

fil_path = "C:/Users/lydia/OneDrive/Documents/GitHub/data5500_fall2024/week5_lists_queues_stacks/states_territories.txt"

#put states into a list without list comprehension
states = []

fil = open(fil_path)

for line in fil.readlines():
    print(line)
    states.append(line.strip())

print(states)

##list comprehension- go straight to the for loop to understand/write
states_t = [line.strip() for line in open(fil_path).readlines()]
print(states_t)

def hello_world(name):
    print("hello"+ name)
hello_world("andy")

#debuggers
#3 commands
#step over, step into, step out
#resume goes to next dot
#step over goes to next line of code
#step into goes into the function that it's breaking
#look at variables as they are created
#watch expression- inject code as you do it

#json for homework
