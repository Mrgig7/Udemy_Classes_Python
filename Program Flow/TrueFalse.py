# day = 'Monday'
day = 'Saturday'
temperature = 30
# raining = True
raining = False

# if day == 'Saturday' and temperature > 27 and not raining:
if (day == 'Saturday' and temperature > 27) or not raining:
    print("Go Swimming")
else:
    print('Learn Python')

if 0:
    print("True")
else:
    print("False")

name =input("Please enter your name")

if name:
    print("Hello,{}".format(name))
else:
    print("Are you man with no name?")

