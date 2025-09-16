income = 45000
print("given income:", income)

def calculate_tax(income):
    brackets = [
        (10000, 0.0),
        (10000, 0.1),
        (float("inf"), 0.2)
    ]

    tax = 0
    for limit, rate in brackets:
        taxable = min(income, limit)
        tax += taxable * rate
        income -= taxable
        if income <= 0:
            break
    return tax

tax_to_pay = calculate_tax(income)
print("total tax to pay is:", tax_to_pay)
