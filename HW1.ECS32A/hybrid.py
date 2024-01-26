#Homework 1 Challenge Problem hybrid.py
#Liana Williams
#
#Help user decide whether to buy a hybrid car
cost = float(input("Cost of car:"))
miles = float(input("Miles driven per year:"))
gas = float(input("Cost of gas:"))
fuel_ef = float(input("Fuel efficiency (mpg):"))
resale = float(input("Estimated resale value after 5 years:"))

five_gas = (miles/fuel_ef)*(gas*5) #formula for depreciation value after 5 years
five_car = cost-resale #formula for cost to drive car for five year period
five_total = five_gas + five_car #total car

print(f"Five year gas cost: {five_gas}")
print(f"Five year car cost: {five_car}")
print(f"Five year total cost: {five_total}")
