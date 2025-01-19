initial_investment = float(input("Enter the initial investment: "))
annual_interest_rate= float(input("Enter the annual interest rate(in %):"))
year=int (input("Enter the number of years:"))

print("\nYear\tAmount")
amount=initial_investment
for year in range(0,year):
    amount+=amount*(annual_interest_rate/100)
    print(year+1, "\t", round(amount,2))
