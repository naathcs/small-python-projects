# Import necessary libraries 
from currency_converter import CurrencyConverter


c = CurrencyConverter()
currencies = c.currencies

# Let user choose currency from and to convert
def get_user_input():

    while True:
        try:
            print('What is the amount you want to convert? (e.g., 100.00)')
            amount = float(input())

            if amount == 0:
                print('Amount cannot be zero. Please try again!')
                continue # Continue loop if the amount in not valid
            break # If amount is valid, break loop and go to next code section

        except ValueError:
            print('Please enter a valid amount!')



    # Check if currency input is available in library

    print('Choose the currency you want to convert FROM?\n' '(e.g., USD, CAD, EUR, BRL)')
    currencyFrom = input()[:3].upper()
    while currencyFrom not in currencies: 
        print('Invalid entry. Please try again')
        print('Choose the currency you want to convert FROM?\n' '(e.g., USD, CAD, EUR, BRL)')
        currencyFrom = input()[:3].upper()


    print('Choose the currency you want to convert TO?\n' '(e.g., USD, CAD, EUR, BRL)')
    currencyTo = input()[:3].upper()
    while currencyTo not in currencies:
        print('Invalid entry. Please try again')
        print('Choose the currency you want to convert TO?\n' '(e.g., USD, CAD, EUR, BRL)')
        currencyTo = input()[:3].upper()

    #return variables
    return amount, currencyFrom, currencyTo


# Convert the currency
def currency_conversion():

    amount, currencyFrom, currencyTo = get_user_input()

    conversionResult = c.convert(amount, f'{currencyFrom}', f'{currencyTo}')
    print(f'Your conversion is: {conversionResult:.2f} {currencyTo}')


# Show the Conversion Rate and the date this conversion is from

while True:

    currency_conversion()
    print('\nWould you like to run another conversion? (Y/N)')
    answer = input().strip().upper()[:1]

    while answer not in ('Y','N'):
        print('\nInvalid Entry. Please try again.')             
        print('\nWould you like to run another conversion? (Y/N)')
        answer = input().strip().upper()[:1]

    if answer == 'N':
            break