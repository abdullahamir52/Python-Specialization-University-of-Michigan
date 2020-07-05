def computepay(h,r):
    if (h>40):
    	pay = ((h-40)*(1.5*r)) + (40*r)
    else:
    	pay = (h*r)
    return pay

hrs = input("Enter Hours:")
rate = input("Enter rate:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error! Please enter a numeric input!")
    quit()
p = computepay(h,r)
print("Pay",p)
