def sum_of_square_series(number):
    if number == 0:
        return 0
    else:
        return (number * number) + sum_of_square_series(number - 1)

num = int(input("Enter the positive number: "))
total = sum_of_square_series(num)
print(f"The sum of series up to {num} = {total}")
