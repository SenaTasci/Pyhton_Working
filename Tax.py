﻿income = float(input("Enter the annual income: "))

if income <= 85528 :
    tax = income*0.18 - 556
    
elif income > 85528 :
    tax = income*0.32 + 14839

tax = round(tax, 0)
print("The tax is:", tax, "thalers")
