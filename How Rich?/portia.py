# File Name: portia.py
# Author Name: Lindsey Kim
# Date: 9/17/2020
# Course: COSC 1
# Short Description: This calculates the year that Brutus' wealth surpasses Portia's wealth.

BRUTUS_INITIAL_DEPOSIT = 1.00
BRUTUS_INTEREST_RATE = 0.05
brutus_wealth = BRUTUS_INITIAL_DEPOSIT

PORTIA_INITIAL_DEPOSIT = 100000.00
PORTIA_INTEREST_RATE = 0.04
portia_wealth = PORTIA_INITIAL_DEPOSIT

year = 0

while brutus_wealth <= portia_wealth:  # stops when Brutus' wealth exceeds Portia's wealth
    brutus_wealth = brutus_wealth * (1 + BRUTUS_INTEREST_RATE)  # increases Brutus' wealth by the interest rate
    portia_wealth = portia_wealth * (1 + PORTIA_INTEREST_RATE)  # increases Portia's wealth by the interest rate
    year += 1  # increases the current year to the next year

print("In the year " + str(year) + ", Brutus' wealth exceeded Portia's wealth for the first time. ")
print("Portia's wealth was " + str(portia_wealth) + " and Brutus' wealth was " + str(brutus_wealth) + ".")
