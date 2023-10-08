##BMI Calculator: Develop a Body Mass Index (BMI) calculator that takes a person's weight and
##height and calculates their BMI
## 
## Ref -- https://www.calculatorsoup.com/calculators/health/bmi-calculator.php
##


def calculate_bmi(weight_kg, height_m):
    try:
        # Calculate BMI using the formula: BMI = weight (kg) / (height (m) * height (m))
        bmi = weight_kg / (height_m * height_m)
        return bmi
    except ZeroDivisionError:
        return print("Height cannot be zero. Please enter a valid height.")

def main():

    print("Welcome to the BMI Calculator!")
    try: 
        weight_kg = float(input("Enter your weight in kilograms: "))
        height_m = float(input("Enter your height in meters: "))

        bmi = calculate_bmi(weight_kg, height_m)

        if isinstance(bmi, float):
            print(f"Your BMI is: {bmi:.2f}")
        else:
            print(bmi)
    
    except ValueError:
        return print("Values must to be a float. Please enter a valid value.")

if __name__ == "__main__":
    main()


##Adults
## below 18.5 is underweight
## between 18.5 and 24.9 is healthy
## between 25 and 29.9 is overweight
## of 30 or over is obese