#Calculate income tax for the given income by adhering to the rules below
#Taxable Income	Rate (in %)
#First $10,000	0
#Next $10,000	10
#The remaining	20



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
