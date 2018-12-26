Height = int(input("Fill in your height (cm)"))
we = int(input("Fill in your weight (kg)"))

BMI = int((we*10000)/(Height*Height))
print("Your BMI is", BMI)

if BMI < 16:
    print("Severely underweight")
elif 16 <= BMI < 18.5:
    print("Underweight")
elif 18.5 <= BMI < 25:
    print("Normal")
elif 25 <= BMI < 30:
    print("Overweight")
else:
    print("Obese")