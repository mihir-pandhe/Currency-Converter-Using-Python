import requests


def get_live_exchange_rate(from_currency, to_currency):
    api_key = "74cb2f8726a2b15f71f0e7b7"
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if "conversion_rates" not in data:
            raise ValueError("Invalid response from exchange rate API.")
        return data["conversion_rates"].get(to_currency, None)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching exchange rate: {e}")
        return None


def convert_currency(amount, from_currency, to_currency):
    rate = get_live_exchange_rate(from_currency, to_currency)
    if rate is None:
        return None, None
    return amount * rate, rate


def validate_currency(currency):
    supported_currencies = ["USD", "EUR", "GBP", "JPY", "CAD", "INR"]
    return currency in supported_currencies


def get_user_input():
    while True:
        from_currency = input(
            "Enter the source currency (e.g., USD, EUR, GBP, JPY, CAD, INR): "
        ).upper()
        if validate_currency(from_currency):
            break
        else:
            print("Invalid currency. Please enter a valid currency code.")

    while True:
        to_currency = input(
            "Enter the target currency (e.g., USD, EUR, GBP, JPY, CAD, INR): "
        ).upper()
        if validate_currency(to_currency):
            break
        else:
            print("Invalid currency. Please enter a valid currency code.")

    while True:
        try:
            amount = float(input("Enter the amount to be converted: "))
            break
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")

    return from_currency, to_currency, amount


def main():
    print("Currency Converter")

    while True:
        from_currency, to_currency, amount = get_user_input()

        converted_amount, rate = convert_currency(amount, from_currency, to_currency)

        if converted_amount is not None:
            print(
                f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}"
            )
            print(f"Exchange Rate: 1 {from_currency} = {rate:.4f} {to_currency}")
        else:
            print("Invalid currency conversion request.")

        another_conversion = (
            input("Do you want to perform another conversion? (yes/no): ")
            .strip()
            .lower()
        )
        if another_conversion != "yes":
            break


if __name__ == "__main__":
    main()
