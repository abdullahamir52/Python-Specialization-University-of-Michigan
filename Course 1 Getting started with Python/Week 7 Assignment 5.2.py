largest=None
smallest=None
while True:
    num = input('Enter a number:')
    if (num == 'done'):
        break
    try:
        value = int(num)
    except:
        print('Invalid input')
        continue
    if ((largest is None) and (smallest is None)):
        largest=smallest=value
    elif(value<=smallest):
        smallest=value
    elif(value>=largest):
        largest=value

print("Maximum", largest)
print("Minimum", smallest)
"""
    for i in value: 
        if l is 0:
            l=i
        elif i> l:
            l=i
    for j in value: 
        if s is 0:
            s=j
        elif j<s:
            s=j  
"""

"""
while True:
    sval = input('Enter a number:')
    
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input!')
        continue
    # print(fval)
    num = num + 1
    tot = tot + fval
    avg = tot/num

print('All done!')
print('Total',tot,'Count',num,'Average', avg)
"""