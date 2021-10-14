print('This is my tip calculater for the success after prison dinner party!')
# this is the command for the total price of our bill 
bill = float(input("what is the total bill amount?: "))
bill_f = float(bill)
# here is the option to apply a tip
tip = float(input('How much do want to leave your server as a tip?: '))
tip_f = float(tip)
# tax applied to bill 
tax = 0.1
# total amount of people splitting the bill
number_of_people = int(input('How many people are splitting the bill?: '))
number_people_float = float(number_of_people)
# the amount of total bill
bill_amt_with_tip = bill_f * (tip_f/100)
# total after taxes
total = bill + (bill_amt_with_tip * tax)
split_bill = total/number_of_people
print(f'Thanks for celebrating with us everbody in your party should pay ${split_bill} and your grand total is ${total}')