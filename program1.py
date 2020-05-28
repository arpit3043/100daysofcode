p = float(10000)
t = float(5)
r = float(12)

amount = p*((1+(r/100))**t)
intrest = amount - p
print("amount is %.2f" %amount)
print("compount intrest is %.2f" %intrest)