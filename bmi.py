userWeight:float = float(input("Enter Weight in Kgs: "))
userHeight:float = float(input("Enter Height in meters: "))
userBMI = float(userWeight/(userHeight*userHeight))
print(f"Your BMI is: {userBMI}")