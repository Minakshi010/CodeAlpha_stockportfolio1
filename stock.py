import tkinter as tk
from tkinter import messagebox, filedialog
import csv

# Stock prices
stock_prices = {
    "RELIANCE": 2500,
    "TCS": 3800,
    "INFY": 1500
}

portfolio = {}

# Add stock
def add_stock():
    stock = stock_entry.get().upper()
    qty = quantity_entry.get()

    if stock not in stock_prices:
        messagebox.showerror("Error", "Stock not available!")
        return

    if not qty.isdigit():
        messagebox.showerror("Error", "Enter valid quantity!")
        return

    portfolio[stock] = int(qty)

    display_text.delete("1.0", tk.END)
    display_text.insert(tk.END, f"{portfolio}")

# Save CSV
def save_csv():
    print("Portfolio Data:", portfolio)  # DEBUG LINE

    if not portfolio:
        messagebox.showwarning("Warning", "Portfolio empty!")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV Files", "*.csv")]
    )

    if not file_path:
        return

    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Stock", "Quantity", "Total Value"])

        for stock, qty in portfolio.items():
            value = stock_prices[stock] * qty
            writer.writerow([stock, qty, value])

    messagebox.showinfo("Success", "File Saved Successfully!")

# GUI
root = tk.Tk()
root.title("Test Portfolio")

tk.Label(root, text="Stock").pack()
stock_entry = tk.Entry(root)
stock_entry.pack()

tk.Label(root, text="Quantity").pack()
quantity_entry = tk.Entry(root)
quantity_entry.pack()

tk.Button(root, text="Add Stock", command=add_stock).pack()
tk.Button(root, text="Save CSV", command=save_csv).pack()

display_text = tk.Text(root, height=5)
display_text.pack()

root.mainloop()