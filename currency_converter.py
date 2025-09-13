from requests import get
from pprint import PrettyPrinter
from dotenv import load_dotenv

load_dotenv()


API_KEY = ""
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}"

printer = PrettyPrinter()

# Cache dictionary
CACHED_RATES = {}


def get_currencies(base="USD"):
    """
    Fetch conversion rates for the base currency.
    Cache the result so we don't hit the API repeatedly.
    """
    if base in CACHED_RATES:  # check if already cached
        return CACHED_RATES[base]

    url = f"{BASE_URL}/latest/{base}"
    data = get(url).json()

    if "conversion_rates" not in data:
        print("Error fetching currencies:", data)
        return {}

    conversion_rates = data["conversion_rates"]
    CACHED_RATES[base] = conversion_rates  # store in cache
    return conversion_rates


def print_currencies(currencies):
    """
    currencies.items() already gives a list of (key, value) pairs → like [("USD", 1), ("EUR", 0.85)].
    sorted(...) just sorts them alphabetically by the key (currency code).
    So when you loop directly with for code, rate in ..., Python unpacks each tuple into code and rate.
    used enumerate(sorted_currencies) it would instead give you an index plus the tuple
    then it has to be
     for i, (code, rate) in enumerate(sorted_currencies):
        print(i, code, rate)

    0 EUR 0.85
    1 NGN 1500
    2 USD 1

    """
    sorted_currencies = sorted(currencies.items())
    for code, rate in sorted_currencies:
        print(f"{code} - {rate}")


def exchange_rate(currency1, currency2):
    rates = get_currencies(currency1)

    if not rates or currency2 not in rates:
        print("Invalid currency:", currency2)
        return None

    rate = rates[currency2]
    print(f"{currency1} -> {currency2} = {rate}")
    return rate


def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)
    if rate is None:
        return

    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount.")
        return

    converted_amount = rate * amount
    print(f"{amount} {currency1} is equal to {converted_amount:.2f} {currency2}")
    return converted_amount


def main():
    base_currency = "USD"
    currencies = get_currencies(base_currency)

    print("Welcome to the currency converter!")
    print("List - lists the different currencies")
    print("Convert - convert from one currency to another")
    print("Rate - get the exchange rate of two currencies")
    print()

    while True:
        command = input("Enter a command (q to quit): ").lower()

        if command == "q":
            break
        elif command == "list":
            print_currencies(currencies)
        elif command == "convert":
            currency1 = input("Enter a base currency: ").upper()
            amount = input(f"Enter an amount in {currency1}: ")
            currency2 = input("Enter a currency to convert this amount to: ").upper()
            convert(currency1, currency2, amount)
        elif command == "rate":
            currency1 = input("Enter a base currency: ").upper()
            currency2 = input(f"Enter a currency to convert {currency1} to: ").upper()
            exchange_rate(currency1, currency2)
        else:
            print("Unrecognized command!")


if __name__ == "__main__":
    main()