# import os
# os.system("clear")
coffee = {"coffee": 2.5, "cappuccino": 7, "mocha": 4.2, "latte": 2, "Tea": 3.3, "water": 3}
print("======= welcome in Alhadad coffee shop ==================== ")
print("======= Here You can Get what you want types of coffee ==================== ")

drink_list = list(coffee.keys())
order = input(f"What do you want to drink {drink_list}==>").lower()
if order in coffee:
    print(f"Your order is {order}")
    cost = (input(f"The price of ({order})is ({coffee[order]}) Enter the money==>"))
    if float(cost) == coffee[order]:
        print("=============================")
        print("take your drink thank you")
        print("=============s================")
    elif float(cost) > coffee[order]:
        which = float(cost) - coffee[order]
        print("=============================")
        print(f"Take your drink and here your change {which}")
        print("=============================")
    elif float(cost) < coffee[order]:
        print("=============================")
        print(f"The money is not enough take your money ")
        print("=============================")
else:
    print("========== These drinks are not here thank you, go to another coffee shop Nooooow ================")
