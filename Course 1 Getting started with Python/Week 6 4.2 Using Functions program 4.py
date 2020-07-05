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
