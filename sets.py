# sets are unordered, unindexed, and there are no duplicates
fruits = {"apple", "banana", "orange", "cherry", "orange"} 

print(fruits) # won't return "orange" twice

#check if item exists
if "apple" in fruits:
    print("apple is in fruits")
else:
    print("apple is not in fruits")

print("apple" in fruits)

# add items

fruits.add("pear")

print(fruits)

# add multiple items
fruits.update(["kiwi", "watermelon"])

print(fruits)

#removing items
fruits.remove("pear")

print(fruits)

# if you're not sure if an item exists you can use discard() to avoid errors
fruits.discard("papaya")
# fruits.remove("papaya") - this would throw an error since "papaya" doesn't exist in the set

#set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1.union(set2)) # will ignore duplicates 3 and 4
print(set1.intersection(set2)) # will return the duplicates only


print(set1.difference(set2)) # display whats in set 1 that isn't in set 2

print("----------MINI CHALLENGE-------------")
invited_friends = {"Alex", "Sam", "Leo", "Mina"}
rsvps = {"Mina", "Sam", "Jordan"}

print(f"Here is everyone who was invited: {invited_friends.union(rsvps)}")
print(f"Here is everone that RSVPed: {rsvps}")
print(f"Here are the people who haven't responded yet: {invited_friends.difference(rsvps)}")

#add 2 names to invited friends
invited_friends.update(["Ed", "Kathi"])

#one of the people canceled - delete them
rsvps.discard("Mina")
print("Mina cancelled")
print(f"New RSVP List: {rsvps}")

#print number of confirmed attendees
print(len(rsvps))

if "Leo" in rsvps:
    print("Leo is coming")
else:
    print("Leo has not RSVP'd yet")
