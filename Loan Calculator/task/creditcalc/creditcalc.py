import math
import argparse
import sys


def differentiate_payment(payment_type, monthly_payment, principal, periods, interest):
    overpayment = 0
    i = interest / (12 * 100)
    monthly_payments = []

    if payment_type == "annuity" and principal is not None and periods is not None:
        i1n = (1 + i) ** periods
        annuity_payment = math.ceil(principal * ((i * i1n) / (i1n - 1)))
        print(f"Your annuity payment = {annuity_payment}!")
        overpayment = (annuity_payment * periods) - principal
        print(f"Overpayment = {overpayment}")
    elif payment_type == "annuity" and principal is None and periods is not None:

        i1n = (1 + i) ** periods
        principal = math.floor(monthly_payment / (i * i1n / (i1n - 1)))
        print(f"Your loan principal = {principal}!")
        overpayment = monthly_payment * periods - principal
        print(f"Overpayment = {overpayment}")
    elif payment_type == "annuity" and principal is not None and periods is None:
        x = monthly_payment / (monthly_payment - (i * principal))
        base = i + 1
        periods = math.ceil(math.log(x, base))
        n_years = periods // 12
        rest_months = periods - n_years * 12
        years_msg = "" if n_years == 0 else (f"{n_years} year" + (" " if n_years == 1 else "s "))
        and_msg = "and " if (n_years > 0 and rest_months > 0) else ""
        months_msg = "" if rest_months == 0 else (f"{rest_months} month" + (" " if rest_months == 1 else "s "))
        print(f"It will take {years_msg}{and_msg}{months_msg}to repay this loan!")
        overpayment = periods * monthly_payment - principal
        print(f"Overpayment = {overpayment}")
    elif payment_type == "diff" and periods is not None:
        for n in range(1, periods + 1):
            result = math.ceil(principal/periods + (i * (principal - (principal * (n - 1) / periods))))
            monthly_payments.append(result)
            print(f"Month {n}: payment is {result}")
            overpayment = sum(monthly_payments) - principal
        print()
        print(f"Overpayment = {overpayment}")

    else:
        print("Incorrect parameters.")


parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--payment", type=int)
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
args = parser.parse_args()

if len(sys.argv) == 5 and args.interest is not None and (args.type == "annuity" or args.type == "diff"):
    differentiate_payment(args.type, args.payment, args.principal, args.periods, args.interest)
else:
    print("Incorrect parameters.")
