# Import necessary libraries 
from currency_converter import CurrencyConverter


c = CurrencyConverter()

# Let user choose currency from and to convert
def get_user_input():
    print('What is the amount you want to convert? ')
    amount = float(input())

    print('Choose the currency you want to convert FROM?\n' \
    '(e.g., USD, CAD, EUR, BRL)')
    currencyFrom = input()[:3].upper()

    print('Choose the currency you want to convert to?\n' \
    '(e.g., USD, CAD, EUR, BRL)')
    currencyTo = input()[:3].upper()

    #return variables
    return amount, currencyFrom, currencyTo


# Convert the currency
def currency_conversion():

    amount, currencyFrom, currencyTo = get_user_input()
    
    # Check currency
    currencies = c.currencies
    
    if currencyFrom in currencies and currencyTo in currencies:
        conversionResult = c.convert(amount, f'{currencyFrom}', f'{currencyTo}')
        print(f'Your conversion is: {conversionResult:.2f} {currencyTo}')
    else:
        print('One or more entries are not valid')


# Show the Conversion Rate and the date this conversion is from
while True:
    currency_conversion()
    print('\nWould you like to run another conversion? (Y/N)')
    answer = input()[:1].upper()

    if answer == 'N':
        break
    elif answer != 'Y':
        print('Please enter a valid answer.')