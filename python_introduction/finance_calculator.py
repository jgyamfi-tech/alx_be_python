# Prompt user for their monthly income
monthly_income = float(input("Enter your monthly income: "))  # Convert input to float for decimal values

# Prompt user for their total monthly expenses
monthly_expenses = float(input("Enter your total monthly expenses: "))  # Convert input to float for decimal values

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Project annual savings with interest
annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)  # 5% annual interest applied to yearly savings

# Display results
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${annual_savings:.2f}.")
