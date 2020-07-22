# =============================================================================
# Program 1
# =============================================================================

x=5
print('Hello')
def print_lyrics():
    print('My name is Abdullah')
# If we don't invoke the function print_lyrics then, it just stores the function.
print('Yo')
x=x+2
print(x)
print_lyrics()

# =============================================================================
# Program 2
# =============================================================================

def greet(lang):
# arguments are input values. e.g. 'es', 'fr'
# parameters are a variable which we use in the function definition. e.g. 'lang'
# It is a 'handle' that allows the code in the fn to access the arguments
# for a particular fn invocation
    if lang=='es':
        print('Hola')
    elif lang=='fr':
        print('Bonjour')
    else:
        print('Hello')
greet('en')
greet('es')
greet('fr')

# =============================================================================
# Program 3
# =============================================================================

def greet():
    return 'Hello'
# often a function will take its argument, do some calculation and return a
# value in the expression
print(greet(), 'Glenn')
print(greet(), 'Sally')

# =============================================================================
# Program 4
# =============================================================================

# a return command stops, determines the residual value and gives it back to us.
# once we can use the return command, the function stops there.
def greet(lang):
    if lang=='es':
        return'Hola'
    elif lang=='fr':
        return'Bonjour'
    else:
        return'Hello'
print(greet('en'), 'Glenn')
print(greet('es'), 'Sally')
print(greet('fr'), 'Michael')

# =============================================================================
# Program 5
# =============================================================================

def addtwo(a,b):
    added = a + b
    return added
x = addtwo(3,5)
print(x)

# Function with a return value = 'fruitful' Function
# Function without a return value= 'Non-fruitful' Function
