#program using value keywords
x = 12
y = 6
z = x < y
print(z)
w = x > y
print(w)


# program using logical operaters
x = 15
y = 30
# and conditions
#both need to be true to execute if block
if x < 5 and y <50:
    print(x+15)

# or condition
# atleast 1 need to be true to execute if block
if x > 5 or y <100:
    print(x+15)

# not condition
# condition must be false
if not x:
    print(x+15)

# program using conditional keyword
x = 75
if x > 100:
    print('x is greater than 100')
elif x > 50:
    print('x is greater than 50 but less than 100')
else:
    print('x is less than 50')


#program using break condition
numbers = [10,20,30,60,190,66] 
for i in numbers:
    if i > 100:
        break
    print('current number',i)  