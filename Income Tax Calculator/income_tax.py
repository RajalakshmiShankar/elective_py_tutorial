
income=float(input("Enter Your Income :"))

if income < 0:
    print("Invalid income")
else:
    tax = 0
    if income <= 300000:
        tax = 0  
    elif income <= 600000:
        tax = (income - 300000) * 0.05  
    elif income <= 900000:
        tax = (300000 * 0.05) + (income - 600000) * 0.1  
    elif income <= 1200000:
        tax = (300000 * 0.05) + (300000 * 0.1) + (income - 900000) * 0.15  
    elif income <= 1500000:
        tax = (300000 * 0.05) + (300000 * 0.1) + (300000 * 0.15) + (income - 1200000) * 0.2  
    else:
        tax = (300000 * 0.05) + (300000 * 0.1) + (300000 * 0.15) + (300000 * 0.2) + (income - 1500000) * 0.3  

print("The Income Tax for",income ,"is",tax)