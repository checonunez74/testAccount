'''
This program demonstrates the Account class.
creates an Account object with an account id of 1122,
a balance of $20,000, and an annual interest rate of 4.5%.
Use the withdraw method to withdraw $2,500, use the deposit method
to deposit $3,000, and print the id, balance, monthly interest rate,
and monthly interest.
'''

import accountQuiz

def main():
    # Get the client's account id number
    id_num = int(input('Enter your account number: '))
    
    # Get the starting balance.
    start_bal = float(input('Enter your starting balance: '))

    # Create a BankAccount object.
    checking = accountQuiz.Account(start_bal)

    # Deposit the user's paycheck.
    pay = float(input('How much do you want to deposit? '))
    print('I will deposit that into your account.')
    checking.deposit(pay)

    # Monthly interest rate.
    

    # Display the balance.
    print('Your account balance is $', \
          format(checking.get_balance(), ',.2f'),
          sep='')

    # Get the amount to withdraw.
    cash = float(input('How much would you like to withdraw? '))
    print('I will withdraw that from your account.')
    checking.withdraw(cash)

    # Display the balance.
    print('Your account balance is $', \
          format(checking.get_balance(), ',.2f'),
          sep='')
    '''
    # Print Interest rate
    print('Your interest rate is $', \
          format(checking.get_interest(), ',2.f'),
          sep='')
    '''
# Call the main function.
main()
