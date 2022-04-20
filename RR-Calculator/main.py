import tkinter as tk
from tkinter import ttk
import math

def calc_stop_loss():
    option_price = float(option_price_input.get()) * 100.0
    stop_loss = (option_price * .10)
    result = math.floor(option_price - stop_loss) / 100.0
    stop_loss_result_label.config(text=f"{result}")
        

def calc_take_profit():
    option_price = float(option_price_input.get()) * 100.0
    take_profit = (option_price * .20)
    result = math.floor(option_price + take_profit) / 100.0
    take_profit_result_label.config(text=f"{result}")
    
def calc_rr():
    try:
        calc_take_profit()
        calc_stop_loss()
    except ValueError:
        error_label = ttk.Label(window, font="Arial, 10", text="Please enter a number (example: 0.54).")
        error_label.grid(column=1, row=8, padx=10, pady=10)
        error_label.after(5000, error_label.destroy)
        error_label['background']="#383838"
        error_label['foreground']="#FF8C32"
        take_profit_result_label.config(text="")
        stop_loss_result_label.config(text="")
        
# Window
window = tk.Tk()
window.title("Options Risk Calculator")
window.geometry("300x400")
window.resizable(0,0)
window['background']="#383838"
window.iconphoto(False, tk.PhotoImage(file=r'C:\Users\anais\Documents\MyPythonProjects\RR-Calculator\Stocks-icon.png'))

# option price label
option_price_label = ttk.Label(window, font="Arial, 10", text="Option Price: (example: 0.54, or 1.24)")
option_price_label.grid(column=1, row=1, padx=10, pady=10)
option_price_label['background']="#383838"
option_price_label['foreground']="#F2F2F2"

# program description
program_description_label = ttk.Label(window, font="Arial, 8", text="This calculator will take the price of an option (call or put)\nand calculate 20% take profit, and a 10% stop loss.")
program_description_label.grid(column=1, row=0, padx=10, pady=10)
program_description_label['background']="#383838"
program_description_label['foreground']="#F2F2F2"

# option price
option_price_input = ttk.Entry(window, width=15)
option_price_input.grid(column=1, row=2, padx=10, pady=10)
option_price_input['background']="#383838"

#take profit label
take_profit_label = ttk.Label(window, font="Arial, 10", text="Take Profit:")
take_profit_label.grid(column=1, row=3, padx=10, pady=10)
take_profit_label['background']="#383838"
take_profit_label['foreground']="#F2F2F2"

take_profit_result_label = ttk.Label(window, font="Arial, 12", text="")
take_profit_result_label.grid(column=1, row=4, padx=5, pady=5)
take_profit_result_label['background']="#383838"
take_profit_result_label['foreground']="#F2F2F2"

#stop loss label
stop_loss_label = ttk.Label(window, font="Arial, 10", text="Stop Loss:")
stop_loss_label.grid(column=1, row=5, padx=10, pady=10)
stop_loss_label['background']="#383838"
stop_loss_label['foreground']="#F2F2F2"

stop_loss_result_label = ttk.Label(window, font="Arial, 12", text="")
stop_loss_result_label.grid(column=1, row=6, padx=5, pady=5)
stop_loss_result_label['background']="#383838"
stop_loss_result_label['foreground']="#F2F2F2"

#Calc button
calc_btn = ttk.Button(text="Calculate", command=calc_rr)
calc_btn.grid(column=1, row=7, padx=10, pady=20)

window.mainloop()