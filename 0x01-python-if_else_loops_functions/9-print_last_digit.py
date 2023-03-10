#!/usr/bin/python3
def print_last_digit(number):
    last_digit = abs(number) % 10
    if number < 0:
        last_digit = -abs(last_digit)
    print(f"{last_digit:d}", end="")


num = int(input("Enter a number: "))
print_last_digit(num)
