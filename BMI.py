#BMI = (weight in pounds * 703) / (height in inches * height in inches)
name = input("Enter your name: ")

weight = int(input("Enter your weight in pounds: "))

height = int(input("Enter your height in inches: "))

print(weight)
print(height)

BMI = (weight * 703) / (height  * height )
print(BMI)

if BMI>0:
    if (BMI < 18.5):
        print(name + ", You are underweight.")
    elif(BMI < 24.9):
        print(name + ", You are normal weight")
    elif(BMI < 29.9):
        print(name + ", You are over weight")
    elif(BMI < 34.9):
        print(name + ", You are Obese")
    elif(BMI < 39.9):
        print(name + ", You are Severly Obese")          
    else:
        print(name + ", You are morbidly Obese")    
else:
    print("Enter valid input")        
