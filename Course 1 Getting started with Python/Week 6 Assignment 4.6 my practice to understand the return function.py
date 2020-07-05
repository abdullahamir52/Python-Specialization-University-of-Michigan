# This user-defined function takes the value of var1 and floats it then assigns it to var2
# Then it multiplies var2 by 10 and assigns it to pay
# Then the return value/residual value is pay
def computepay(var1):
    var2 = float(var1)
    pay = var2*10
    return pay

# Abovementioned user-defined function is used below

# This statement will take the input value of h and assign it into var1
var1 = input('h:')
# then computepay function will take the value of var1 as its argument and execute the codes within it
p = computepay(var1)
print("Pay",p)
