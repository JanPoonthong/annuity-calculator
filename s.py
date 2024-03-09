def calculate_s(interest_rate, periods):
    annuity = (((1 + interest_rate) ** periods) - 1) / interest_rate
    return round(annuity, 6)


interest_rate = float(input("Enter the interest rate per period: "))
periods = int(input("Enter the number of periods: "))

s_amount = calculate_s(interest_rate, periods)
print(f"The s amount is: {s_amount}")
