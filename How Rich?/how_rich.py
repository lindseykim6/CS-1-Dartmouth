# File Name: how_rich.py
# Author Name: Lindsey Kim
# Date: 9/17/2020
# Course: COSC 1
# Short Description: This calculates the wealth Brutus amasses in 2018 using a while loop.
#

BRUTUS_INITIAL_DEPOSIT = 1.00
BRUTUS_INTEREST_RATE = 0.05
current_year = 0
brutus_wealth = BRUTUS_INITIAL_DEPOSIT

while current_year < 2018:  # stops before the current year can increase to 2019
    brutus_wealth = brutus_wealth * (1 + BRUTUS_INTEREST_RATE)  # increases Brutus' wealth by the interest rate
    current_year += 1  # increases the current year to the next year

print("At year " + str(current_year) + " Brutus' wealth was " + str(brutus_wealth) + ".")
