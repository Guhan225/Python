try:
    a=int(input("Enter A: "))
    b=int(input("Enter B: "))
    result=a/b
    print("Result: ",result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")
except ValueError:
    print("Invalid input:,Please enter a number")