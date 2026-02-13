print ("hello boy")
name =(input("whats your name" ))
if name == "ben" :
    evil_status = input ('are u evil??????')
    if evil_status == "yes":
        print("get out")
        exit()
    else :
        print("your good welcome\n")
    
menu = 'cappuccino\n' "black coffee\n" "latte\n" "mocha\n" "americano\n"
print ('what would you like to order\n' + menu)
order = input()
if order == "cappuccino":
    price = 10
elif order == "black coffee": price = 7
elif order == "latte": price = 12
elif order == "mocha": price = 15
elif order == "americano": price = 8
else :
    print("sorry we dont have that")
quantity = float(input("how many would you like? "))
total = price * quantity
print("your total is  \n $" + str(total))
print ("thank you for your order " + name)
