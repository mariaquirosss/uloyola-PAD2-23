## Factorial calculation: Create a function that calculates the factorial of a given number


def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

def factorial2(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        result = 1
        i = 1
        while i <= n:
            result *= i
            i += 1
        return result


# Example usage:
num = 5  # Replace with the number for which you want to calculate the factorial
result = factorial(num)
print(f"The factorial of {num} is {result}")