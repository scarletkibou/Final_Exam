from function import *


print("Welcome to Milk Tea shop!!!")
check=input("Would you like a Milk Tea?(y/n):")
if check=="y":
    toppings=get_topping()
    total_cost = calculate_total_cost(toppings)
    check_bill(total_cost,toppings)
else: print("Hope to see you next time!!!")
    
    
        
        


