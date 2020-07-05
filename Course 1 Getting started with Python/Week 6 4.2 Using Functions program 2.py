def greet(lang):
# arguments are input values. e.g. 'es', 'fr'
# parameters are a variable which we use in the function definition. e.g. 'lang'
# It is a 'handle' that allows the code in the fn to access the arguments for a particular fn invocation
    if lang=='es':
        print('Hola')
    elif lang=='fr':
        print('Bonjour')
    else:
        print('Hello')
greet('en')
greet('es')
greet('fr')
