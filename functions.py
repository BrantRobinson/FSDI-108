#function is a block of code that runs when called

#simple function
def my_function(): # define function
    print("This is my function") #function code


#function with a parameter
def print_full_name(fname, lname):
    print(f"this is my name: {fname} {lname}")

#funtion that returns something
def get_full_name():
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    return f"{fname} {lname}"

def print_full_name_again():
    full_name = get_full_name()
    print(f"your full name is: {full_name}")


print_full_name_again()


my_function() #calling the function
print_full_name("Brant", "Robinson")

#combine words function
def combine_words(word1, word2, word3):
    words = [word1, word2, word3]
    combined = " ".join(words)
    return combined

result = combine_words("Hello", "World", "Earth")
print(result)

def future_age(current_age):
    return current_age + 10

age_in_10 = future_age(46)
print(f"Age in 10 years = {age_in_10}")


    
