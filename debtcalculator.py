'''
A simple program created to calculate the credit card balance after one year if the person only pays back the minimum payments each month.
'''
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
monthlyInterestRate = annualInterestRate / 12.0
minimumMonthlyPayment = monthlyPaymentRate * balance
totalPaid = 0
month = 1
while month <= 12:
    minPayment = monthlyPaymentRate * balance 
    balance -=  minPayment 
    balance += (annualInterestRate/12.0)*balance 
    totalPaid += minPayment 
    month += 1
    remainingbalance = balance
print ('Remaining balance:', round(remainingbalance,2))