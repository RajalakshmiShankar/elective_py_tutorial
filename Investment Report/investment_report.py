
#ROI formula: ROI = ((current_value - investment_amount) / investment_amount) * 100

investment_amount = float(input("Enter the initial investment amount: "))
current_value = float(input("Enter the current value of the investment: "))

roi = ((current_value - investment_amount) / investment_amount) * 100

print("Return on Investment (ROI): {:.2f}".format(roi))

#print("Return on Investment (ROI):",roi:.2f)
