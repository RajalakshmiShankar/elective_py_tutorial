initial_investment = float(input("Enter the initial investment: "))
annual_interest_rate= float(input("Enter the annual interest rate(in %):"))
year=int (input("Enter the number of years:"))
annual_interest_rate/=100

print("\nYear\tAmount")
amount=initial_investment
for year in range(0,year):
    amount+=amount*annual_interest_rate
    print(f"{year+1}\t{amount:.2f}")
