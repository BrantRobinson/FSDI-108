
# Create a tuple with 5 items
travel_bag = ("passport", "toothbrush", "shoes", "charger", "sunglasses")

# Print the 2nd and 4th items
print("2nd item:", travel_bag[1])
print("4th item:", travel_bag[3])

# Check if "shoes" is in the bag
if "shoes" in travel_bag:
    print("You're ready to walk!")
else:
    print("You forgot your shoes!")

# Make a new tuple called "essentials"
essentials = ("underwear", "shampoo", "pillow")

# Combine to make final_bag
final_bag = (travel_bag + essentials)
print(final_bag)

# Print how many items are in your bag
print(f"You have {len(final_bag)} items in your bag")

# Print last item in your bag
print(f"The last item in your bag is {final_bag[-1]}")

