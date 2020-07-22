"""
link: https://trinket.io/python/79b285a420

Write a program which repeatedly reads numbers until the user enters
#“done”. Once “done” is entered, print out the total, count, and average
#of the numbers. If the user enters anything other than a number, detect
#their mistake using try and except and print an error message and skip to
#the next number.

"""


sum = 0
count = 0
average = 0

while True:
  try:
    x = input("Enter a number: ")
    if (x == "done"):
     break
    value = float(x)
    sum = value + sum
    count = count + 1
    average = sum / count
  except:
    print("Invalid input.")
print ('Total',sum,'Count', count,'Average', average)


# ALTERNATE WAY TO SOLVE THIS
num = 0
tot = 0.0
avg = 0.0
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
