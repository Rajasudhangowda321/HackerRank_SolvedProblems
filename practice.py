meal_coat=float(input())
tip_percent=int(input())
tax_percent=int(input())
tip_percent=meal_coat*(tip_percent/100)
tax_percent=meal_coat*(tax_percent/100)
total_cost=meal_coat+tip_percent+tax_percent
print(round(total_cost))
