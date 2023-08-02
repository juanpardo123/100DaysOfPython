# Instructions
# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill.

# Small Pizza: $15

# Medium Pizza: $20

# Large Pizza: $25

# Pepperoni for Small Pizza: +$2

# Pepperoni for Medium or Large Pizza: +$3

# Extra cheese for any size pizza: + $1

# Example Input
# size = "L"
# add_pepperoni = "Y"
# extra_cheese = "N"
# Example Output
# Your final bill is: $28.

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
def pizzaOrder(qSize, qAdd_pepperoni, qExtra_cheese):
    orderTotal = 0
    if(qSize.lower() == 's'):
        orderTotal = 15
        if(qAdd_pepperoni.lower() == 'y' ):
            orderTotal += 2
    elif(qSize.lower() == 'm'):
        orderTotal = 20
        if(qAdd_pepperoni.lower() == 'y' ):
            orderTotal += 3
    elif(qSize.lower() == 'l'):
        orderTotal = 25
        if(qAdd_pepperoni.lower() == 'y' ):
            orderTotal += 3
    if(qExtra_cheese.lower() == 'y' ):
            orderTotal += 1
    return orderTotal

print(f'Your final bill is: ${pizzaOrder(size,add_pepperoni,extra_cheese)}')