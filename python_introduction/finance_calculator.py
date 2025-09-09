monthly_income = input("Enter your monthly income: ")
monthly_expenses = input("Enter your total monthly expenses: ")
monthly_savings = int(monthly_income) - int(monthly_expenses)
rate = 0.05
projected_savings = int(monthly_savings) * 12 + (int(monthly_savings) * 12 * float(rate))
print("Your monthly savings are $"+str(monthly_savings))
print("Projected savings after one year, with interest, is: $" + str(projected_savings))