exchange_rates = {
    "USD": {
        "EUR": 0.92360,
        "GBP": 0.77829,
        "JPY": 152.77,
        "CAD": 1.3841,
        "INR": 83.703,
    },
    "EUR": {"USD": 1.0828, "GBP": 0.8425, "JPY": 165.36, "CAD": 1.4982, "INR": 90.62},
    "GBP": {"USD": 1.285, "EUR": 1.1867, "JPY": 196.33, "CAD": 1.7799, "INR": 107.56},
    "JPY": {
        "USD": 0.00654,
        "EUR": 0.00605,
        "GBP": 0.00509,
        "CAD": 0.00906,
        "INR": 0.5478,
    },
    "CAD": {"USD": 0.7227, "EUR": 0.6675, "GBP": 0.5620, "JPY": 110.32, "INR": 60.46},
    "INR": {
        "USD": 0.01195,
        "EUR": 0.01103,
        "GBP": 0.00930,
        "JPY": 1.8255,
        "CAD": 0.01655,
    },
}


def get_exchange_rate(from_currency, to_currency):
    return exchange_rates.get(from_currency, {}).get(to_currency, None)


def convert_currency(amount, from_currency, to_currency):
    rate = get_exchange_rate(from_currency, to_currency)
    if rate is None:
        return None
    return amount * rate


def main():
    print("Currency Converter")

    from_currency = input(
        "Enter the source currency (e.g., USD, EUR, GBP, JPY, CAD, INR): "
    ).upper()
    to_currency = input(
        "Enter the target currency (e.g., USD, EUR, GBP, JPY, CAD, INR): "
    ).upper()
    amount = float(input("Enter the amount to be converted: "))

    converted_amount = convert_currency(amount, from_currency, to_currency)

    if converted_amount is not None:
        print(
            f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}"
        )
    else:
        print("Invalid currency conversion request.")


if __name__ == "__main__":
    main()
