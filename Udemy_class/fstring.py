greeting = "Hello"
name = "Tim"
print(greeting+name)
# if we want space, we can add that too

print(greeting + ' ' + name)

age = 24
print(age)

print(type(greeting))
print(type(age))

age_in_words = " 2 years"
#print(name + " is " + age + " years old") old wrong statement
print(name + f" is {age} years old")
print(type(age))

print(f"Pi is approximately {22 / 7:12.50f}")
pi = 22/7
print(f"Pi is approximately {pi:12.50f}")