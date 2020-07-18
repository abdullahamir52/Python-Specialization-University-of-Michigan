# =============================================================================
# Program 1 : Counting numbers
# =============================================================================

zork = 0
# zork is the count variable here

print('Before', zork)

# i is the iteration variable here
for i in [9,41,12,3,74,15]:
    zork = zork + 1
    print (zork, i)
print('After',zork)

# =============================================================================
# Program 2 : summing in a loop
# =============================================================================

total = 0
print('Before', total)
 
for i in [9,41,12,3,74,15]:
    total = total + i 
    print('Current number',i,'Total',total)
print('After', total)

# =============================================================================
# Program 3 : Finding the avg in a loop
# =============================================================================

count = 0
sum = 0 
print('Before', count, sum)

for value in [9,41,12,3,74,15]:
    count = count + 1
    sum = sum + value
    print('Count',count,'Sum',sum,'Value',value)

print('After','Count',count,'Sum',sum,'Avg',sum/count)

# =============================================================================
# Program 4 : Filtering in a loop
# =============================================================================

print('Before')

for value in [9,41,12,3,74,15]:
    if value > 20:
        print('Large number',value)
print('After')


# =============================================================================
# Program 5 : Search using a boolean variable
# =============================================================================

found = False
print('Before', found)

for value in [9,41,12,3,74,15]:
    if value == 3:
        found = True
    print(found,value)
print('After',found)

# =============================================================================
# Program 6 : Finding the smallest value
# =============================================================================

smallest = None
print('Before')

for value in [9,41,12,3,74,15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print('Value',value, 'Smallest',smallest)
print('After', 'Smallest', smallest)
