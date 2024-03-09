def calculate_annuity(interest_rate, periods):
    annuity = (1 - (1 + interest_rate) ** -periods) / interest_rate
    return round(annuity, 6)


interest_rate = float(input("Enter the interest rate per period: "))
periods = int(input("Enter the number of periods: "))

annuity_amount = calculate_annuity(interest_rate, periods)
print(f"The annuity amount is: {annuity_amount}")
