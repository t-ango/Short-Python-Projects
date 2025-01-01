'''
This program calculates the user's Body Mass Index (BMI) based on their
weight in kilograms and height in centimeters. It then categorizes the BMI
into Underweight, Normal, Overweight, or Obese based on standard BMI ranges.
'''
weight = eval (input("Enter your weight in kg"))
height = eval (input("Enter your height in cm"))
heightInMeters = height / 100
bmi = weight/(heightInMeters * heightInMeters)
print ("Your BMI is" , format (bmi , ".2f"))
if bmi < 18.5 :
    print ("Underweight")
elif bmi > 18.5 and bmi < 24.9 :
    print ("Normal")
elif bmi > 25.0 and bmi < 29.9 :
    print ("Overweight")
else :
    print ("Obese")