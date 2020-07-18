# String concatenation
a = 'Hello'
b = a + 'There'
print(b)
c = a + ' ' + 'There'
print(c)

# Using 'in' as a logical operator (returns a logical answer such as T or F)
fruit = 'banana'
'n' in fruit
'm' in fruit
if 'a' in fruit:
    print('Found it!')

# String Comparison
word = 'chuck'
if word == 'banana':
    print('All right, bananas.')
else:
    print('Not banana!')
# String Comparison 2
# plug in chuck, banana, ahuck to see what output is printed
word = 'chuck'
if word < 'banana':
    print('Your word, ' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word, ' + word + ', comes after banana.')
else:
    print('All right, bananas.')

# String Library
""" Python has a number of string functions which are in the string library.
These functions are already built into every string - we invoke them by
appending the function to the string variable. These functions do not modify
the original string, instead they return a new string that has been altered."""
greet = 'Hello Bob.'
zap = greet.lower()
print(zap)
print(greet)
print('Hi There'.lower())

# Searching a Strings
"""We use the find() function to locate a substring within another string.
If not found, then returns -1. String position starts at zero."""
fruit = 'banana'
pos = fruit.find('na')
print(pos)
aa = fruit.find('z')
print(aa)

# Making everything upper case
""" Often we lowercase everything before we use the find function
within a string"""
greet = 'Hello Bob'
nnn = greet.upper()
www = greet.lower()
print(nnn,www)

# search and replace
# this method is case sensitive
greet = 'Hello Bob'
nstr1 = greet.replace('Bob', 'Jane')
nstr2 = greet.replace('o', 'X')
nstr3 = greet.replace('O', 'X')
print(nstr1)
print(nstr2)
print(nstr3)

# Stripping Whitespace
# lstrip() and rstrip() to remove Whitespace on left and right side
# strip() to remove both sides
greet = '   Hello bob   '
greet.lstrip()
greet.rstrip()
greet.strip()

# Prefixes
line = 'Please have a nice day!'
line.startswith('Please')
line.startswith('p')

# Parsing and Extracting
"""We want to capture the uct.ac.za, not including the space afterwards.
So we use the find functions to find relevant positions. Also, we can use
where to start counting in find function (e.g. atpos). Then we add 1 with
atpos to start counting after the @ position."""
data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
spacepos = data.find(' ', atpos)
print(spacepos)
host = data[atpos + 1 : spacepos]
print(host)
