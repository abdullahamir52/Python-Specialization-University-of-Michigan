
"""
Finishing the iteration with continue
The continue statement ends the current iteration and jumps to the top of the loop
and starts the next iteration
"""


while True: 
    line = input('>')
    if line [0] == '#':
        continue
# when the program faces a continue statement, it goes up to the top of the loop
    if line == 'done':
        break
# when the program faces a break statement, it exits the loop
    print(line)
print('Program execution is over!')
