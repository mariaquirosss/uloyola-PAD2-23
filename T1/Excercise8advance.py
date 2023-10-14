##Dice simulator: Write a program that simulates the roll of two dice and calculates the sum of
##the values obtained.
## Displate
## Execute to install the lib - py -m pip install matplotlib

import random
import matplotlib.pyplot as plt

def roll_two_dice():
    die1 = random.randint(1, 6)  # Roll the first die
    die2 = random.randint(1, 6)  # Roll the second die
    total = die1 + die2
    return total

def main():

    # 
    result = []
    num_exec = 1000
    
    for _ in range(num_exec):
       result.append(roll_two_dice())

    # Create plot
    plt.hist(result, bins=range(2, 14), align='left', rwidth=0.8)

    # Add labels and title
    plt.xlabel('Amout of values')
    plt.ylabel('Frecuency')
    plt.title('Rolling two dice'+str(num_exec))

    # Show grafic
    plt.show()

    print()


if __name__ == "__main__":
    main()