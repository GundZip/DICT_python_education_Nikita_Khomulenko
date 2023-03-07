import math
from translations import *


print(welcome_message)
print(calculation_options)

calculation_type = input()
if calculation_type == 'n':
    print(principal_prompt)
    loan_principal = float(input())
    print(payment_prompt)
    monthly_payment = float(input())
    print(interest_prompt)
    interest = float(input()) / 1200

    n = math.ceil(math.log(monthly_payment / (monthly_payment - interest * loan_principal), 1 + interest))
    if n > 0:
        years, months = divmod(n, 12)
        if years == 0:
            print(year_prompt.format(months))
        elif months == 0:
            print(mount_prompt.format(years))
        else:
            print(m_y_prompt.format(years, months))
    else:
        print("The loan cannot be repaid with this monthly payment!")

elif calculation_type == 'a':
    print(principal_prompt)
    loan_principal = float(input())
    print(periods_prompt)
    n = int(input())
    print(interest_prompt)
    interest = float(input()) / 1200

    annuity_payment = loan_principal * (interest * (1 + interest)**n) / ((1 + interest)**n - 1)

    years, months = divmod(n, 12)
    if years == 0:
        print(periods_m_y.format(round(annuity_payment), months))
    elif months == 0:
        print(periods_m_y.format(round(annuity_payment), years))
    else:
        print(periods_m_and_y.format(round(annuity_payment), years, months))

elif calculation_type == 'p':
    print(payment_prompt)
    annuity_payment = float(input())
    print(periods_numb)
    n = int(input())
    print(interest_prompt )
    interest = float(input()) / 1200

    loan_principal = annuity_payment / ((interest * (1 + interest)**n) / ((1 + interest)**n - 1))

    years, months = divmod(n, 12)
    if years == 0:
        print(l_principal.format(round(loan_principal), months))
    elif months == 0:
        print(l_principal.format(round(loan_principal), years))
    else:
        print(principal_m_y.format(round(loan_principal), years, months))

elif calculation_type == 'd':
    print(principal_prompt)
    loan_principal = float(input())
    print(num_periods)
    n = int(input())
    print(interest_prompt)
    interest = float(input()) / 1200

    total_payment = 0

    for month in range(1,n +1):
        differentiated_payment = loan_principal / n + interest * (loan_principal - loan_principal * (month - 1) / n)
        total_payment += differentiated_payment
        print(mount_pay.format(month, math.ceil(differentiated_payment)))

        overpayment = total_payment - loan_principal
        print(overpayment_result.format(round(overpayment)))

else:
    print(Error)
