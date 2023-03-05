print('Power by Stell \n'
      'Hello')
principal = float(input("Enter the loan principal: "))
interest_rate = float(input("Enter the interest rate: "))

months = int(input("Enter the number of months: "))

monthly_payment = principal * (interest_rate * (1 + interest_rate) ** months) / ((1 + interest_rate) ** months - 1)
total_payment = monthly_payment * months

for i in range(1, months + 1):
    interest = principal * interest_rate
    principal -= monthly_payment - interest
    print(f"Month {i}: repaid {round(monthly_payment, 2)}")

print(f"\nThe loan has been repaid!\nTotal payment: {round(total_payment, 2)}")
print ('Have a nice day')
