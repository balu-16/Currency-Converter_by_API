import requests
import tkinter as tk
from tkinter import ttk, messagebox

API_KEY = "9139b84f42fe19123faca2e1"  # Replace with your actual API key
API_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"

def get_currencies():
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        return list(data.get("conversion_rates", {}).keys())
    else:
        messagebox.showerror("Error", "Failed to fetch currencies.")
        return []

def convert_currency():
    from_currency = from_currency_var.get()
    to_currency = to_currency_var.get()
    amount = amount_var.get()
    
    try:
        amount = float(amount)
        url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_currency}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            rate = data.get("conversion_rates", {}).get(to_currency)
            if rate:
                converted_amount = amount * rate
                result_var.set(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
            else:
                messagebox.showerror("Error", "Invalid currency conversion.")
        else:
            messagebox.showerror("Error", "Failed to fetch exchange rate.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount.")

# GUI Setup
root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x300")
root.resizable(False, False)

currencies = get_currencies()

from_currency_var = tk.StringVar(value="USD")
to_currency_var = tk.StringVar(value="EUR")
amount_var = tk.StringVar()
result_var = tk.StringVar()

# Widgets
frame = ttk.Frame(root, padding=20)
frame.pack(fill="both", expand=True)

ttk.Label(frame, text="Amount:").grid(row=0, column=0, pady=5, sticky="w")
ttk.Entry(frame, textvariable=amount_var, width=20).grid(row=0, column=1, pady=5)

ttk.Label(frame, text="From Currency:").grid(row=1, column=0, pady=5, sticky="w")
ttk.Combobox(frame, textvariable=from_currency_var, values=currencies, state="readonly").grid(row=1, column=1, pady=5)

ttk.Label(frame, text="To Currency:").grid(row=2, column=0, pady=5, sticky="w")
ttk.Combobox(frame, textvariable=to_currency_var, values=currencies, state="readonly").grid(row=2, column=1, pady=5)

ttk.Button(frame, text="Convert", command=convert_currency).grid(row=3, columnspan=2, pady=10)

ttk.Label(frame, textvariable=result_var, font=("Arial", 12, "bold"), foreground="blue").grid(row=4, columnspan=2, pady=10)

root.mainloop()
