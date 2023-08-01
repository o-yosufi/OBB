Sure! Here's a simple example of a calculator in Python that takes two numbers as input:

# Function to perform addition
def add(num1, num2):
    return num1 + num2

# Function to perform subtraction
def subtract(num1, num2):
    return num1 - num2

# Function to perform multiplication
def multiply(num1, num2):
    return num1 * num2

# Function to perform division
def divide(num1, num2):
    return num1 / num2


# Getting input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Performing the operations
("Addition:", add(num1, num2))
("Subtraction:", subtract(num1, num2))
("Multiplication:", multiply(num1, num2))
("Division:", divide(num1, num2))
```

In this example, we define four separate functions `add`, `subtract`, `multiply`, and `divide` to perform the corresponding operations. The `input` function is used to get the numbers from the user, and `float` is used to convert the input to a floating-point number (allowing decimal values). The operations are then performed using the input numbers and the respective functions, and the results are printed out.