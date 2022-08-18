#A lot of cell phones have tip calculators. Write one. Ask the user for 
#the price of the meal and
#the percent tip they want to leave. 
#Then print both the tip amount and the total bill with the
#tip included

meal=int(input("price of meal"))

tip=int(input("tip percent"))

tip_amount=(tip*meal)/100

print("Price of meal is "+str(meal))

print("Tip amount is "+str(tip_amount))