income=int(input("Enter Your Income :"))
if income<=250000:
    tax=0
elif income > 250000 and income <= 500000:
    tax=(income-250000)*0.05
elif income>500000 and income <=1000000:
    tax=(income-500000)*0.2 + 250000*0.05
else:
    tax=(income-1000000)*0.3 +500000*0.2+250000*0.05
print("The Income Tax for",income ,"is",tax)