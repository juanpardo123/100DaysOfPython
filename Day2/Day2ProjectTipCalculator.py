#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to The Tip Calculator 3000!!!!")
promptBill = input('Please input the total bill amount:')
promptPeople = input('Please input the total amount of people:')
promptTipPercentage = input('Please input the tip percentage you want to give:')

def tipCalc(bill,people,decTipPercent):
    tipPercent = (float(decTipPercent) / 100) 
    total = (float(bill)/int(people)) * (1 + tipPercent)
    return round(total, 2) 

print(tipCalc(promptBill, promptPeople, promptTipPercentage))