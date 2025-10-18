# While loops - repeats a block of code as long as a condition is True
# CAUTION - if the condition never becomes False then you'll get an infinite loop
print("--------------while loops-----------")
count = 1

while count <= 5:
    print("The count is: ",count)
    count += 1

# Break to stop loop
print("----------break-------------")

count = 1

while count <= 10:
    if count == 5:
        print("Breaking at 5")
        break
    print("the count is: ", count)
    count += 1

# using Skip continue to skip interaction
print("----------continue-------------")

count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print("The count is ", count)

# else with a while loop
# the else block runs when the loop condition is false

# print("-------------else--------------")
# count = 1
# while count < 3:
#     count += 1
#     print("The count is: ", count)
# else:
#     print("loop finished")

# # mini challenge - password checker
# print("----------mini challenge #1------------")

# while True:
#     password = input("Enter your password: ")
#     if password == "secret123":
#         print("Access Granted!")
#         break
#     print("Wrong, try again")

#try to do it in as few lines of code as possible


# for loops - used for looping over a sequence:
# list, tuple, dictionary, strings, etc

#loop through a list
fruits = ["apple", "banana", "grapes", "oranges"]

for item in fruits:
    print(item)

#loop through a string
myString = "hello"
for letter in myString:
    print(letter)

#using range()
#range() generates a sequnce of unmbers

print("-------ranges--------")
for x in range(5):
    print(x)

print("--------ranges 3-10 step 2")

for x in range(3,10,2): #(start, stop, step)
    print(x)

for x in range(3):
    print(x)
else: # you don't really need this loop
    print("loop done")

# break and continue in for loops
print("---- for loop with break and continue -----")
for x in range(10):
    if x == 5: #skip 5
        continue
    elif x == 8: # end at 7
        break
    print(x)

#mini challenge #2
print("--------mini challenge # 2-----------")
words = ["super", "excellent", "outstanding", "nope", "the", "if", "whatever", "me", "coolio"]
word_with_5_or_more = []
for word in words:
    length = len(word)
    if length >=5:
        word_with_5_or_more.append(word)
print(f"There are {len(word_with_5_or_more)} words with 5 or more letters in your list")
print(f"Here they are:")
for word in word_with_5_or_more:
    print(word)

       







