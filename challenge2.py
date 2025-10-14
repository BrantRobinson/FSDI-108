#mini challenge 2
def get_values():
    x = int(input("Enter x value: "))
    y = int(input("Enter y value: "))
    results = subtraction(x,y)
    print(f"{x} - {y} = {results}")

def subtraction(x, y):
    results = x-y
    return results

get_values()




