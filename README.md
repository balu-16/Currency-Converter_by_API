# Currency Converter

This Python program provides a simple command-line currency converter. It uses the ExchangeRate-API to fetch exchange rates and perform currency conversions.

## Features

* **List Currencies:** Displays a list of all available currencies supported by the API.
* **Get Exchange Rate:** Retrieves and displays the current exchange rate between two specified currencies.
* **Convert Currency:** Converts a given amount from one currency to another using the current exchange rate.
* **User-Friendly Interface:**  Provides a menu-driven command-line interface for easy interaction.
* **Error Handling:** Includes basic error handling to catch invalid input and API errors.

## How to Use

1. **API Key:** You'll need an API key from ExchangeRate-API.  You can obtain one by signing up for a free account at [https://www.exchangerate-api.com/](https://www.exchangerate-api.com/).  **Replace `"9139b84f42fe19123faca2e1"` in the code with your actual API key.**

2. **Installation:**  No special installation is required besides having Python 3 installed.

3. **Running the Program:**
    ```bash
    python currency_converter.py
    ```

4. **Interaction:** Follow the prompts in the console to choose an action (list currencies, get exchange rate, convert currency) and provide the necessary input.

## Example Usage
Currency Converter Menu:

List all available currencies
Get exchange rate between two currencies
Convert currency q. Quit Enter your choice: 1
Available currencies:
AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, 1  CUC, CUP, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, INR, IQD, IRR, ISK, JMD, JOD, JPY, KES, KGS, KHR, KMF, KPW, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, 2  MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, 3  SDG, SEK, SGD, SHP, SLL, SOS, SRD, SSP, STN, SVC, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, USD, UYU, UZS, VES, VND, VUV, WST, XAF, XCD, XDR, XOF, XPF, 4  YER, ZAR, ZMW, ZWL   
1.
github.com
github.com
2.
learn.microsoft.com
learn.microsoft.com
3.
marketplace.whmcs.com
marketplace.whmcs.com
4.
github.com
github.com

Currency Converter Menu:

List all available currencies
Get exchange rate between two currencies
Convert currency q. Quit Enter your choice: 2 Enter the currency you want to convert from (e.g., USD): USD Enter the currency you want to convert to (e.g., EUR): EUR
Exchange rate from USD to EUR: 0.9215

Currency Converter Menu:

1. List all available currencies
2. Get exchange rate between two currencies
3. Convert currency
q. Quit
Enter your choice: 3
Enter the currency you want to convert from (e.g., USD): USD
Enter the currency you want to convert to (e.g., EUR): EUR
Enter the amount to convert: 10
10 USD is equal to 9.22 EUR.

Currency Converter Menu:

1. List all available currencies
2. Get exchange rate between two currencies
3. Convert currency
q. Quit Enter your choice: q
Exiting the program. Goodbye!

## Dependencies

* `requests`:  Install it using pip: `pip install requests`

## Future Improvements

* **Error Handling:** More comprehensive error handling for various API responses and edge cases.
* **Input Validation:**  More robust input validation to prevent invalid currency codes or amounts.
* **Caching:** Implement caching of exchange rates to reduce API calls and improve performance.
* **Data Persistence:**  Option to save and load preferred currency pairs or conversion history.
* **User Interface:**  Consider creating a GUI for a more visually appealing and user-friendly experience.

## Contributing

Contributions are welcome! Feel free to submit pull requests or open issues.
