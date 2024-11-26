try:
    num=int(input("Enter a number: "))
    result=14/num
    print("Result: ",result)
except ValueError:
    print("Invalid input! Please enter a valid number")
except ZeroDivisionError:
    print("Error! Divisible by zero is not allowed")
else:
    print("No Exception Occured")
finally:
    print("This block always runs")
    