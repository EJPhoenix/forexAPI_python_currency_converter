from forex_python.converter import CurrencyRates
from currency_codes import get_currency_by_code, CurrencyNotFoundError

# INSTANTIATE A CURRENCY RATES CLASS
c = CurrencyRates()


# print(get_currency_by_code('USD').code)
# print(currency_info.code)


def currency_converter():
    # USERS STARTING CURRENCY
    base_cur = input('What currency are you exchanging? ').upper()
    # print(base_cur)
    try:
        get_currency_by_code(base_cur)
    except CurrencyNotFoundError:
        print("Invalid. Re-Start and use valid Currency Code")
        exit()

    # USERS TARGET CURRENCY
    destination_cur = input('What currency do you want to receive? ').upper()
    # print(destination_cur)
    try:
        get_currency_by_code(destination_cur)
    except CurrencyNotFoundError:
        print("Invalid. Re-Start and use valid Currency Code")
        exit()

    # AMOUNT OF SOURCE CURRENCY BEING EXCHANGED
    try:
        input_amount = float(input('How much does you want to exchange? '))
        # print(input_amount)
        while input_amount <= 0:
            input_amount = float(input('Invalid entry. Please try again: '))
    except ValueError:
        print("Invalid entry. Please Restart")
        exit()

    print('Please wait... Verifying transaction')
    conversion = (c.convert(base_cur, destination_cur, input_amount))

    rounded_final_currency = round(conversion, 2)

    print(f"You exchanged: {input_amount} {base_cur}\nWhich equals: {rounded_final_currency} {destination_cur}")


currency_converter()
