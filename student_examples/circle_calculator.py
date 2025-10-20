# @Author - Omar

# Circle Calculator

# Step 1: Define functions
def area(radius):
    return 3.14159 * radius * radius

def circumference(radius):
    return 2 * 3.14159 * radius

# Step 2: Greet the user

print("Welcome to the Circle Calculator!")
print("Enter -1 to exit.\n")

# Step 3: Keep asking for a radius until user enters -1
while True:
    radius = float(input("Enter radius: "))
    if radius == -1:
        print("Goodbye!")
        break

    if radius > 0:
        a = area(radius)
        c = circumference(radius)
        print("Area:", a)
        print("Circumference:", c, "\n")
    else:
        print("Please enter a positive number.\n")