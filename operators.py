### Types of operators ###
###1. Arithmetic (math)
x = 6
y = 4
res = 0
res = x + y
print(res)
res = x - y
print(res)
res = x / y
print(res)
res = x // y #divide and drop the decimal
print(res)
res = x * y
print(res)
res = x % y #remainder
print(res)
res = x ** y #Exponent
print(res)

###2. Assignment (put values into a variable)
x = 5 #assign 1
print(x)
x += 1 #add 1 to x
print(x)
x -= 1 #subtract 1 from x
print(x)
x *= 2 #x times 2
print(x)
x /= 2 #x divided by 2
print(x)

###3. Comparison (checkc if things are the same or diffierent)
# == equal
# != not equal
# <> less than, greater than

###4. Logical (true or false conditions)
x = 3
y = 10
z = 3
print("Logical")
print (x == y and y == z) # and - both must be true
print (x == y or x == z) # or - at least 1 must be true
print (not x == z) # not - flips true to false and vice versa


###5. Identity (checks if 2 things are the same object)
x = 3
y = 3
print("Identity")
print(x is y)
print(x is not y)


###6. Membership (checks if things are in a list)

x = [1,2,3,4,5,6] # creates a list of numbers
print("Membership")
print(4 in x) #true
print(10 in x) #false
print(10 not in x) #true

#list
mix_list = [1, "apple", 3.5, True]
print("Mixed List")
print(mix_list)

print(mix_list[1]) # print just the second item
print(mix_list[-2]) # print just the second from the right

mix_list[1] = "Cherry" # change apple to cherry
print(mix_list)

#add to the list
mix_list.append("Orange") # add to the end of the list
print(mix_list)
mix_list.insert(2, "Kiwi") #add kiwi to position 2 and push everything else right
print(mix_list)
mix_list.remove("Kiwi") # you have to call the value to remove, not the index
print(mix_list)
mix_list.pop(2) # remove at index 2 or pop() would remove the last item
print(mix_list)

print("Orange" in mix_list) #Check if Orange is in the list
if "Orange" in mix_list: 
    print("Orange is in the list")

print(len(mix_list))

check = ("Orange" in mix_list)
if check:
    print("its in the list")

print ("----------------")
print("SHOPPING LIST CHALLENGE")
shopping_list = ["cereal", "fruit", "bread", "pizza", "milk"]
print(shopping_list)
print(f"First Item: {shopping_list[0]}, Last Item: {shopping_list[len(shopping_list)-1]}")
print(shopping_list)
shopping_list[1] = "cheese" #replace second item with cheese
print("replace second item")
print(shopping_list)
shopping_list.append("ice cream")
print("add ice cream to the end of list")
print(shopping_list)
print("remove bread from the list")
shopping_list.remove("bread")
print(shopping_list)
print(f"Shopping list has {len(shopping_list)} items")




