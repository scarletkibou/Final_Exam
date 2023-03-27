Topping = {
    "Bubble": 5,
    "Grass Jelly": 10,
    "Red Bean": 15,
    "Wip Cream": 15
}


def calculate_total_cost(toppings):
    total_cost = 25
    for topping in toppings:
        total_cost += Topping[topping]
    return total_cost

def get_topping():
    num_toppings = int(input("How many toppings do you want (up to 2)? "))
    toppingc=[]
    if num_toppings > 0 and num_toppings <=2:
        print("We have 3 toppings 1.Bubble 2.Grass Jelly 3.Red Bean 4.Wip Cream") 
        for i in range (num_toppings):
            x=input("Select your topping(1/2/3/4):")
            if x=="1":
                toppingc.append("Bubble")
            elif x=="2":
                toppingc.append("Grass Jelly")
            elif x=="3":
                toppingc.append("Red Bean")
            elif x=="4":
                toppingc.append("Wip Cream")
    elif num_toppings==0:
        total_cost=25
    else:
        print("invalid input")
    return toppingc


def check_bill(total_cost,toppings):
    print(f"Great! Your order with {', '.join(toppings)} costs ${total_cost}. Enjoy your milk tea!")
    return (f"Great! Your order with {', '.join(toppings)} costs ${total_cost}. Enjoy your milk tea!")
    