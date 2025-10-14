def check_for_even(num):
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

num_to_check = int(input("enter a number: "))
check_for_even(num_to_check)