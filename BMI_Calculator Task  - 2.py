def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    return weight / (height_m ** 2)

while True:
    try:
        height = float(input("Enter your height in centimeters: "))
        weight = float(input("Enter your weight in kilograms: "))
    except ValueError:
        print("Invalid input. Please provide valid numbers.")
        continue

    if height <= 0 or weight <= 0:
        print("Height and weight must be positive values.")
        continue

    bmi = calculate_bmi(weight, height)
    print(f"Your BMI is: {bmi:.2f}")

    if bmi < 18.5:
        print(" Yiu are in Underweight.")
    elif 18.5 <= bmi < 25:
        print(" You are in Normal weight.")
    elif 25 <= bmi < 30:
        print("You are in Overweight.")
    else:
        print("You are in Obese.")
    break
