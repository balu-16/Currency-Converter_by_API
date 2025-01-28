import requests

def list_currencies(api_key):
    """Fetch and display all available currencies."""
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        currencies = list(data.get('conversion_rates', {}).keys())
        print("\nAvailable currencies:")
        print(", ".join(currencies))
    else:
        print(f"Error: {response.status_code} - {response.text}")

def get_exchange_rate(api_key, from_currency, to_currency):
    """Fetch the exchange rate between two currencies."""
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        rates = data.get('conversion_rates', {}).get(to_currency)
        if rates:
            print(f"\nExchange rate from {from_currency} to {to_currency}: {rates:.4f}")
        else:
            print("Error: Currency conversion rate not found.")
    else:
        print(f"Error: {response.status_code} - {response.text}")

def convert_currency(api_key, from_currency, to_currency, amount):
    """Convert a given amount from one currency to another."""
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        rates = data.get('conversion_rates', {}).get(to_currency)
        if rates:
            converted_amount = amount * rates
            print(f"\n{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}.")
        else:
            print("Error: Currency conversion rate not found.")
    else:
        print(f"Error: {response.status_code} - {response.text}")

def main():
    api_key = "9139b84f42fe19123faca2e1"  # Replace with your actual API key

    while True:
        print("\nCurrency Converter Menu:")
        print("1. List all available currencies")
        print("2. Get exchange rate between two currencies")
        print("3. Convert currency")
        print("q. Quit")

        choice = input("Enter your choice: ").strip().lower()

        if choice == "1":
            list_currencies(api_key)
        elif choice == "2":
            from_currency = input("Enter the currency you want to convert from (e.g., USD): ").upper()
            to_currency = input("Enter the currency you want to convert to (e.g., EUR): ").upper()
            get_exchange_rate(api_key, from_currency, to_currency)
        elif choice == "3":
            from_currency = input("Enter the currency you want to convert from (e.g., USD): ").upper()
            to_currency = input("Enter the currency you want to convert to (e.g., EUR): ").upper()
            try:
                amount = float(input("Enter the amount to convert: "))
                convert_currency(api_key, from_currency, to_currency, amount)
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        elif choice == "q":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or q.")

if __name__ == "__main__":
    main()
