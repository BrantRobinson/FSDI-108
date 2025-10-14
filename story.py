first_name = 'Brant'
age = 46
location = 'San Diego'
sport = 'Tennis'
wife = 'Francesca'
kids = 5
cool = True

#f format
print (f"""My name is {first_name}. 
I'm {age} years old. 
I live in {location} with my wife, {wife}, and our {kids} kids. 
My favorite sport is {sport}. 
Am I the coolest dad ever?: {cool}""")

print (f"My name is {first_name}. I'm {age} years old. I live in {location} with my wife, {wife}, and our {kids} kids. My favorite sport is {sport}. Am I the coolest dad ever?: {cool}")

#join method - this method is impractical for this
words = ['My','name', 'is', first_name,'and', "I'm", str(age), 'years', 'old.']
sentance = " ".join(words)
print(sentance)

# format method
sentance_two = "My name is {}. I'm {} years old. I live in {} with my wife, {}, and our {} kids. My favorite sport is {}. Am I the coolest dad ever?: {}".format(first_name, age, location, wife, kids, sport, cool)
print(sentance_two)