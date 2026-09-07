import tkinter as tk
from tkinter import messagebox
from src.converter import convert_currency

BLACK = "#000000"
BLUE = "#2563EB"
RED = "#DC2626"
WHITE = "#FFFFFF"
LIGHT_GRAY = "#F2F2F2"


def convert():
    try:
        amount = float(amount_entry.get())

        result = convert_currency(
            amount,
            from_currency.get(),
            to_currency.get()
        )

        result_label.config(
            text=f"{amount:.2f} {from_currency.get()} = "
                 f"{result:.2f} {to_currency.get()}",
            fg=WHITE
        )

    except ValueError as error:
        result_label.config(text="Error", fg=RED)
        messagebox.showerror("Error", str(error))


def button_click():
    # Simple click animation
    convert_button.config(bg=RED)
    window.after(100, lambda: convert_button.config(bg=BLUE))

    convert()


# Window
window = tk.Tk()
window.title("Currency Converter")
window.geometry("400x450")
window.configure(bg=BLACK)
window.resizable(False, False)


# Title
tk.Label(
    window,
    text="Currency Converter",
    font=("Arial", 22, "bold"),
    bg=BLACK,
    fg=WHITE
).pack(pady=30)


# Amount
tk.Label(
    window,
    text="Amount",
    bg=BLACK,
    fg=WHITE
).pack()

amount_entry = tk.Entry(
    window,
    font=("Arial", 14),
    bg=LIGHT_GRAY,
    relief="flat"
)
amount_entry.pack(pady=8, ipady=8)


# From currency
tk.Label(
    window,
    text="From",
    bg=BLACK,
    fg=WHITE
).pack()

from_currency = tk.StringVar(value="USD")

tk.OptionMenu(
    window,
    from_currency,
    "USD", "INR", "EUR", "GBP", "JPY"
).pack(pady=8)


# To currency
tk.Label(
    window,
    text="To",
    bg=BLACK,
    fg=WHITE
).pack()

to_currency = tk.StringVar(value="INR")

tk.OptionMenu(
    window,
    to_currency,
    "USD", "INR", "EUR", "GBP", "JPY"
).pack(pady=8)


# Convert button
convert_button = tk.Button(
    window,
    text="Convert",
    command=button_click,
    bg=BLUE,
    fg=WHITE,
    font=("Arial", 12, "bold"),
    relief="flat",
    bd=0,
    width=20
)

convert_button.pack(pady=20)


# Result
result_label = tk.Label(
    window,
    text="",
    font=("Arial", 14, "bold"),
    bg=BLACK,
    fg=WHITE
)

result_label.pack(pady=10)


window.mainloop()