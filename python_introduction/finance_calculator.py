monthly_income = input("Enter your monthly income: ")
monthly_expenses = input("Enter your total monthly expenses: ")
monthly_savings = float(monthly_income) - float(monthly_expenses)
rate = 0.05
projected_savings = float(monthly_savings) * 12 + (float(monthly_savings) * 12 * float(rate))
print("Your monthly savings are $"+str(monthly_savings))
print("Projected savings after one year, with interest, is: $" + str(projected_savings))