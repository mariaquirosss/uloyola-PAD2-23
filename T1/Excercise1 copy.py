##Sum of even numbers: Write a program that sums all the even numbers from 1 to 100.
def calculation():
    # Method 2: Using a while loop
    result = 0
    number = 2
    while number <= 100:
        result += number
    
    number += 2

    print("Sum of even numbers (Method 2):", result) 


def main():
    calculation()

if __name__ ==  "__main__":
    main()