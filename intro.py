first_name = 'Brant'
last_name = 'Robinson'
space = ' '
print(first_name + space + last_name)
print (False)
# Comment
"""
Multi Line Comment
"""
age = 46
print(first_name + space + last_name + ' is',age,'years old')
print(first_name + space + last_name + ' is ' + str(age) + ' years old')

#python uses snake_case

found = False
print('Did he show up to class', found)

print(type(first_name))
print(type(age))
print(type(found))

#casting - convert different data types
#str() converts to string
#int() converts to integer
age_str = str(age)
print(age, age_str)

print(20 + 20)
print(20 + age)
print(20 + int("20"))
print(20+3.3)

#input method
age_new = int(input("what is your age?"))
print(f"In 10 years you will be {age_new+10} years old")

x = int(input("Enter a first value: "))
y = int(input("Enter a second value: "))
print(f"x + y = {x+y}")





