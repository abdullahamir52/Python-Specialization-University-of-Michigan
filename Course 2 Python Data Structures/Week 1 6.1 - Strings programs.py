# program 1
str1 = 'Hello'
str2 = ' There'
bob = str1 + str2
print(bob)

# program 2
str3 = '123'
bob = str1 + 1
print(bob)
# gives a traceback error.

# program 3
str3 = '123'
x = int(str3) + 1
print(x)

# program 4
fruit = 'banana'
letter = fruit[1]
print(letter)

# program 5
fruit = 'banana'
x = 3
w = fruit[x-1]
print(w)

# A character too far
zot = 'abc'
print(zot[4])
#gives a traceback error

# Len function
fruit = 'banana'
x = len(fruit)
print(x)

#Strings have length
fruit = 'banana'
print(len(fruit))

# Looping through Strings (WHILE LOOP)
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

# Looping through Strings (FOR LOOP)
fruit = 'banana'
for letter in fruit:
    print(letter)

# Looping and counting
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

# Looking deeper into IN
for letter in 'banana':
    print(letter)

# Slicing Strings
s = 'Monty Python'
print(s[0:4])
print(s[6:7])
print(s[6:20])
"""
We can look through any continuous section of a string using the colon operator ' : '
second number is upto but not including > print(s[6:7])
if second number is beyond the end, loop stops at the end > print(s[6:20])
"""

# Slicing Strings 2
s = 'Monty Python'
print(s[:2])
print(s[8:])
print(s[:])
# if you leave the spot open, it assumes to start from the beginning or the end
