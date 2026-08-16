inr_per_usd = 95.24

inr_expense = [100, 200, 300, 400, 500]

def convert_inr_to_usd(inr_amount):
    for amount in inr_amount:
        usd_amount = amount / inr_per_usd
        print(f"INR {amount} is equivalent to USD {usd_amount:.2f}")

convert_inr_to_usd(inr_expense)