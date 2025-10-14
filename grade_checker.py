#mini-challenge
while True:
    try:
        score = int(input("Enter a number between 0 and 100: "))
        if score < 0 or score > 100:
            print("I said to enter a number between 0 and 100. Try again!")
            continue

        if score >= 90:
            print("A")
        elif score >=80:
            print("B")
        elif score >=70:
            print("C")
        elif score >=60:
            print("D")
        else:
            print("F")

        again = input("Would you like to enter another grade (y/n)")
        if again != "y":
            print("bye bye")
            break

    except ValueError:
        print("You obviously don't know what a number is.  Stop trying - you get an F")
        break

    
  
