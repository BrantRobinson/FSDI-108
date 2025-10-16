#Store data in Key: value pairs
#word => meaining like a real life dictionary
#always wrtitten with {}

students = {
    "name": "Brant",
    "age": 46,
    "major": "Physics"
}

print (students)

#acces by key
print(students["age"])

#acces by .get
print(students.get("major"))

#adding items
students["grad_year"] = 2003

print(students["grad_year"])

students["age"] = 55

print(students["age"])

#remove items
students.pop("age")
print(f"This is the dictionary without age: {students}")

#check if something exists
if "age" in students:
    print("Age is in the disctionary")
else:
    print("Age is not in the dictionary")

#nested disctionary
students = {
    "student1": {
        "name": "John",
        "age": 30
    },
    "student2":  {
        "name": "Susie",
        "age": 29
    }
}

print(students["student1"]["name"])


#####    MINI CHALLENGE    ######

print("-----------MINI CHALLENGE---------")

# create a dictionary called report_card
report_card = {
    "name": "Brant",
    "subject": "Physics",
    "grade": (80, 95, 73)
}

#print the students name and subject
print(f"Name: {report_card["name"]}    Subject: {report_card["subject"]}")

#calculate the average of the 3 grades and store the avg in the dictionary

sum = sum(report_card["grade"])

average = sum / len(report_card["grade"])
average = round(average, 2)

# could also use .2f to round (to second decimal place) for display purposes
# print(f"{average:.2f}")

report_card["average"] = average
print(f"Your average is {average}")

#print message based on average
if average >= 90:
    print("Excellent Job!")
elif average >= 70:
    print("Good Job!")
else:
    print("See me after class")

#remove subject and print dictionary

report_card.pop("subject")
print(report_card)