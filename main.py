from forex_python.converter import CurrencyRates

c = CurrencyRates()
# print(c.__dir__())


def currency_converter():
    # USERS STARTING CURRENCY
    base_cur = input('What currency are you exchanging? ').upper()
    # print(base_cur)

    # USERS TARGET CURRENCY
    destination_cur = input('What currency do you want to receive? ').upper()
    # print(destination_cur)

    # AMOUNT OF SOURCE CURRENCY BEING EXCHANGED
    try:
        input_amount = float(input('How much does you want to exchange? '))
        # print(input_amount)
        while input_amount <= 0:
            input_amount = float(input('Invalid entry. Please try again: '))
    except ValueError:
        print("Invalid entry. Please restart")
        exit()

    print('Please wait... Verifying transaction')
    conversion = (c.convert(base_cur, destination_cur, input_amount))
    # base_cur_SYMBOL = c.get_symbol(base_cur)
    # destination_cur_SYMBOL = c.get_symbol(destination_cur)

    rounded_final_currency = round(conversion, 2)

    print(f"You exchanged: {input_amount} {base_cur}\nWhich equals: {rounded_final_currency} {destination_cur}")


currency_converter()
