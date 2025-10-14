# if else statements
# if - checks a condition
#elif (else if) - checks another condition if the first one is False
#else - runs if all other conditions are False

age = int(input("Enter your age: "))
if age < 100:
    if age < 21:
        print("you are a minor without access!")
    else: 
        print("you are old enough but not too old")
elif age == 100:
    print("You lived a century")
else:
    print("you are super old")

x = int(input("enter any number (positive, negative, or 0)"))

if x > 0:
    print(f"{x} is positive")
elif x == 0:
    print(f"{x} is zero")
else:
    print(f"{x} is negative")

if x > 5: print(f"{x} is greater than 5")#short hand if statement

print("even") if x % 2 == 0 else print ("odd")

# nested if statement
e = 12
if e > 0:
    if e < 20:
        print(f"{e} is a positive number less than 20")

# combining conditions
if age >= 21 and age <=26:
    print("you are between 21 and 26 years old")

f = 8
k = 8

def check_equals(x,y):
    if x == y:
        print("hello")
    else:
        print("welcome")

check_equals(f,k)


