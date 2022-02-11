def BMI_Calculator():
    bmi = kg / (m**2)
    if bmi > 30.0:
        print('You are classified as Obese')
    if bmi < 18.5:
        print('You are classified as Underweight')
    return bmi

pounds = float(input('Enter your weight: '))
kg = pounds /  2.20462262
inches = float(input('Enter your height (in inches): '))
m = inches / 39.3700787402
print()
print('BMI = ', round(BMI_Calculator(), 1))
    