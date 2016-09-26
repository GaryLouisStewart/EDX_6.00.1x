# should equate to 31.38
# this is just a mockup of what will eventually become the program to calculate debt based on...

'''
Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

to help you get started here is a rough outline of the stages you should probably follow in writing your code
For each month
Compute the monthly payment based on the previous months balance
Update the outstanding balance by removing the payment then charging interest on the result
Output the month the minimum monthly payment and the remaining balance
Keep track of the total amount of paid over all the past months so far
Print out the result statement with the total amount paid and the remaining balance
Use these ideas to guide the creation of your code

'''

# for each in range(1,13):
#      print('month' + ' ' + str(each) + ' ' + 'Remaining balance: ')

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

def months(start_month, end_month):
    month = start_month
    while True:
        yield month
        if (month) == (end_month):
            return
        month += 1
        if (month > 12):
            month = 1
        print(month)