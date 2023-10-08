##Sum of even numbers: Write a program that sums all the even numbers from 1 to 100.

def func3():

    # Method 3: Using list comprehension and the sum function
    even_numbers = [number for number in range(2, 101, 2)]
    sum_even = sum(even_numbers)

    print("Sum of even numbers (Method 3):", sum_even)

def func2():
    # Method 2: Using a while loop
    sum_even = 0
    number = 2
    while number <= 100:
        sum_even += number
        number += 2

    print("Sum of even numbers (Method 2):", sum_even)


def func1():

    # Method 1: Using a for loop
    sum_even = 0
    for number in range(2, 101, 2):  # Start from 2, go up to 100, increment by 2
        sum_even += number

    print("Sum of even numbers (Method 1):", sum_even)


def main():
    func1()
    func2()
    func3()

if __name__ ==  "__main__":
    main()