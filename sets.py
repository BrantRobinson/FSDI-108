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

all_friends = invited_friends.union(rsvps)
print("Here is everyone who was invited:")
for name in all_friends:
    print(name)

print("Here is everone that RSVPed:")
for name in rsvps:
    print(name)

not_rsvp = invited_friends.difference(rsvps)
num = len(not_rsvp)
print(f"Here are the {num} people who haven't responded yet:")
for name in not_rsvp:
    print(name)

#add 2 names to invited friends
invited_friends.update(["Ed", "Kathi"])

#one of the people canceled - delete them
rsvps.discard("Mina")
print("Mina cancelled")
print("New RSVP List:")
for name in rsvps:
    print(name)

#print number of confirmed attendees
print(f"confirnmed # of attendees: {len(rsvps)}")

if "Leo" in rsvps:
    print("Leo is coming")
else:
    print("Leo has not RSVP'd yet")
