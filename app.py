import os
import requests
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# API configuration
API_KEY = os.getenv("API_KEY", "9139b84f42fe19123faca2e1")
API_BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"

# Currency code to country name mapping
CURRENCY_COUNTRIES = {
    "USD": "United States Dollar",
    "EUR": "Euro",
    "GBP": "British Pound Sterling",
    "JPY": "Japanese Yen",
    "AUD": "Australian Dollar",
    "CAD": "Canadian Dollar",
    "CHF": "Swiss Franc",
    "CNY": "Chinese Yuan",
    "HKD": "Hong Kong Dollar",
    "NZD": "New Zealand Dollar",
    "SEK": "Swedish Krona",
    "KRW": "South Korean Won",
    "SGD": "Singapore Dollar",
    "NOK": "Norwegian Krone",
    "MXN": "Mexican Peso",
    "INR": "Indian Rupee",
    "RUB": "Russian Ruble",
    "ZAR": "South African Rand",
    "TRY": "Turkish Lira",
    "BRL": "Brazilian Real",
    "TWD": "Taiwan New Dollar",
    "DKK": "Danish Krone",
    "PLN": "Polish Zloty",
    "THB": "Thai Baht",
    "IDR": "Indonesian Rupiah",
    "HUF": "Hungarian Forint",
    "CZK": "Czech Koruna",
    "ILS": "Israeli New Shekel",
    "CLP": "Chilean Peso",
    "PHP": "Philippine Peso",
    "AED": "United Arab Emirates Dirham",
    "COP": "Colombian Peso",
    "SAR": "Saudi Riyal",
    "MYR": "Malaysian Ringgit",
    "RON": "Romanian Leu",
    "ARS": "Argentine Peso",
    "BGN": "Bulgarian Lev",
    "ALL": "Albanian Lek",
    "AMD": "Armenian Dram",
    "AZN": "Azerbaijani Manat",
    "BAM": "Bosnia and Herzegovina Convertible Mark",
    "BDT": "Bangladeshi Taka",
    "BHD": "Bahraini Dinar",
    "BIF": "Burundian Franc",
    "BND": "Brunei Dollar",
    "BOB": "Bolivian Boliviano",
    "BSD": "Bahamian Dollar",
    "BWP": "Botswanan Pula",
    "BYN": "Belarusian Ruble",
    "BZD": "Belize Dollar",
    "CDF": "Congolese Franc",
    "CRC": "Costa Rican Colón",
    "CVE": "Cape Verdean Escudo",
    "DJF": "Djiboutian Franc",
    "DOP": "Dominican Peso",
    "DZD": "Algerian Dinar",
    "EGP": "Egyptian Pound",
    "ETB": "Ethiopian Birr",
    "FJD": "Fijian Dollar",
    "GEL": "Georgian Lari",
    "GHS": "Ghanaian Cedi",
    "GMD": "Gambian Dalasi",
    "GNF": "Guinean Franc",
    "GTQ": "Guatemalan Quetzal",
    "HNL": "Honduran Lempira",
    "HRK": "Croatian Kuna",
    "HTG": "Haitian Gourde",
    "IQD": "Iraqi Dinar",
    "IRR": "Iranian Rial",
    "ISK": "Icelandic Króna",
    "JMD": "Jamaican Dollar",
    "JOD": "Jordanian Dinar",
    "KES": "Kenyan Shilling",
    "KGS": "Kyrgystani Som",
    "KHR": "Cambodian Riel",
    "KMF": "Comorian Franc",
    "KWD": "Kuwaiti Dinar",
    "KZT": "Kazakhstani Tenge",
    "LAK": "Laotian Kip",
    "LBP": "Lebanese Pound",
    "LKR": "Sri Lankan Rupee",
    "LYD": "Libyan Dinar",
    "MAD": "Moroccan Dirham",
    "MDL": "Moldovan Leu",
    "MGA": "Malagasy Ariary",
    "MKD": "Macedonian Denar",
    "MMK": "Myanmar Kyat",
    "MNT": "Mongolian Tugrik",
    "MOP": "Macanese Pataca",
    "MUR": "Mauritian Rupee",
    "MVR": "Maldivian Rufiyaa",
    "MWK": "Malawian Kwacha",
    "MZN": "Mozambican Metical",
    "NAD": "Namibian Dollar",
    "NGN": "Nigerian Naira",
    "NIO": "Nicaraguan Córdoba",
    "NPR": "Nepalese Rupee",
    "OMR": "Omani Rial",
    "PAB": "Panamanian Balboa",
    "PEN": "Peruvian Sol",
    "PGK": "Papua New Guinean Kina",
    "PKR": "Pakistani Rupee",
    "PYG": "Paraguayan Guarani",
    "QAR": "Qatari Riyal",
    "RSD": "Serbian Dinar",
    "RWF": "Rwandan Franc",
    "SCR": "Seychellois Rupee",
    "SDG": "Sudanese Pound",
    "SOS": "Somali Shilling",
    "SRD": "Surinamese Dollar",
    "SSP": "South Sudanese Pound",
    "STN": "São Tomé and Príncipe Dobra",
    "SVC": "Salvadoran Colón",
    "SYP": "Syrian Pound",
    "SZL": "Swazi Lilangeni",
    "TND": "Tunisian Dinar",
    "TTD": "Trinidad and Tobago Dollar",
    "TZS": "Tanzanian Shilling",
    "UAH": "Ukrainian Hryvnia",
    "UGX": "Ugandan Shilling",
    "UYU": "Uruguayan Peso",
    "UZS": "Uzbekistan Som",
    "VEF": "Venezuelan Bolívar",
    "VND": "Vietnamese Dong",
    "XAF": "Central African CFA Franc",
    "XCD": "East Caribbean Dollar",
    "XOF": "West African CFA Franc",
    "XPF": "CFP Franc",
    "YER": "Yemeni Rial",
    "ZMW": "Zambian Kwacha",
}


def get_currencies():
    """Fetch all available currencies from the API"""
    response = requests.get(f"{API_BASE_URL}USD")
    if response.status_code == 200:
        data = response.json()
        currencies = list(data.get("conversion_rates", {}).keys())
        return sorted(currencies)
    return []


@app.route('/')
def index():
    """Render the main page with all available currencies"""
    currencies = get_currencies()
    # Create a list of dictionaries with code and name
    currency_data = []
    for code in currencies:
        currency_data.append({
            'code': code,
            'name': CURRENCY_COUNTRIES.get(code, f"Currency ({code})")
        })
    return render_template('index.html', currencies=currencies, currency_data=currency_data)


@app.route('/convert', methods=['POST'])
def convert():
    """Handle currency conversion requests"""
    data = request.json
    from_currency = data.get('from_currency')
    to_currency = data.get('to_currency')
    amount = data.get('amount')

    try:
        amount = float(amount)
        url = f"{API_BASE_URL}{from_currency}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            rate = data.get("conversion_rates", {}).get(to_currency)

            if rate:
                converted_amount = amount * rate
                return jsonify({
                    'success': True,
                    'result': {
                        'amount': amount,
                        'from_currency': from_currency,
                        'to_currency': to_currency,
                        'converted_amount': round(converted_amount, 2),
                        'rate': rate
                    }
                })

        return jsonify({'success': False, 'error': 'Failed to get exchange rate'})
    except ValueError:
        return jsonify({'success': False, 'error': 'Invalid amount'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


@app.route('/get_rate', methods=['POST'])
def get_rate():
    """Handle exchange rate requests"""
    data = request.json
    from_currency = data.get('from_currency')
    to_currency = data.get('to_currency')

    try:
        url = f"{API_BASE_URL}{from_currency}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            rate = data.get("conversion_rates", {}).get(to_currency)

            if rate:
                return jsonify({
                    'success': True,
                    'result': {
                        'from_currency': from_currency,
                        'to_currency': to_currency,
                        'rate': rate
                    }
                })

        return jsonify({'success': False, 'error': 'Failed to get exchange rate'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


@app.route('/all_currencies', methods=['GET'])
def all_currencies():
    """Get a complete list of currencies with additional details if available"""
    currencies = get_currencies()
    return jsonify({
        'success': True,
        'currencies': currencies
    })


if __name__ == '__main__':
    app.run(debug=True)
