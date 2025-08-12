try:
    num1 = int(input("Enter the num1: "))
    num2 = int(input("Enter the num2: "))
    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Can't divide by zero!")
except ValueError:
    print("Error: Please enter a valid number!")