# Welcome Guests : Here is  "Success After Prison Dinner Party"  Tip Calculator. 

# PLEASE INPUT THE TOTAL AMOUNT OF THE BILL
bill = float(input("What is the total bill amount?: "))

# Please add your gratuity amount as tip for your server
tip = int(input("What % tip would you like to give?: "))
tip = float(tip)

# Please input the number of people who will equally split the bill 
number_of_people = int(input('How many people are splitting the bill?: '))
number_people_float = float(number_of_people)

# Tax applied to bill 
tax = 0.1

# Total amount of bill 
total = bill + (bill * tax)
split_bill = total/number_of_people

print(f'Thanks for celebrating with us everyone should pay ${split_bill} and your grand total is ${total}')
