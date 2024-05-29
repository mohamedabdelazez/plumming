import tkinter as tk
from tkinter import ttk, messagebox

def linear_interpolate(x0, y0, x1, y1, x):
    return y0 + (y1 - y0) * ((x - x0) / (x1 - x0))

def get_gpm(sfu, flush_mechanism):
    sfu_to_gpm_flush_tank = {1: 3, 2: 5, 3: 6.5, 4: 8, 5: 9.4, 6: 10.7,7: 11.8,8: 12.8,9: 13.7,10: 14.6,11: 15.4,12: 16,13: 16.5,14: 17,15: 17.5,16: 18,17: 18.4, 18: 18.8, 19: 19.2, 20: 19.6, 25: 21.5, 30: 23.3, 35: 24.9, 40: 26.3, 45: 27.7, 50: 29.1, 60: 32, 70: 35, 80: 38, 90: 41, 100: 43.5, 120: 48, 140: 52.5, 160: 57, 180: 61, 200: 65, 225: 70, 250: 75, 275: 80, 300: 85, 400: 105, 500: 124, 750: 170, 1000: 208, 1250: 239, 1500: 269, 1750: 297, 2000: 325, 2500: 380, 3000: 433, 4000: 535, 5000: 593}
    sfu_to_gpm_flush_valve = {0.5: 1.5, 1.0: 3.0, 2.0: 6.0, 3.0: 9.0, 4.0: 12.0, 5.0: 15.0}
    
    if flush_mechanism == "flush_tank":
        conversion_table = sfu_to_gpm_flush_tank
    elif flush_mechanism == "flush_valve":
        conversion_table = sfu_to_gpm_flush_valve
    else:
        raise ValueError("Invalid flush mechanism type")
    
    if sfu in conversion_table:
        return conversion_table[sfu]
    else:
        sorted_keys = sorted(conversion_table.keys())
        for i in range(len(sorted_keys) - 1):
            if sorted_keys[i] < sfu < sorted_keys[i + 1]:
                x0, y0 = sorted_keys[i], conversion_table[sorted_keys[i]]
                x1, y1 = sorted_keys[i + 1], conversion_table[sorted_keys[i + 1]]
                return linear_interpolate(x0, y0, x1, y1, sfu)
        raise ValueError("SFU value out of range")

def calculate_gpm():
    try:
        sfu = float(sfu_var.get())
        flush_mechanism = flush_mechanism_var.get()
        gpm = get_gpm(sfu, flush_mechanism)
        result_var.set(f"GPM: {gpm}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

app = tk.Tk()
app.title("Plumbing GPM Calculator")

ttk.Label(app, text="SFU:").grid(column=0, row=0, padx=10, pady=10)
sfu_var = tk.StringVar()
ttk.Entry(app, textvariable=sfu_var).grid(column=1, row=0, padx=10, pady=10)

ttk.Label(app, text="Flush Mechanism:").grid(column=0, row=1, padx=10, pady=10)
flush_mechanism_var = tk.StringVar(value="flush_tank")
flush_mechanism_combobox = ttk.Combobox(app, textvariable=flush_mechanism_var, values=["flush_tank", "flush_valve"])
flush_mechanism_combobox.grid(column=1, row=1, padx=10, pady=10)

result_var = tk.StringVar()
ttk.Label(app, textvariable=result_var).grid(column=0, row=2, columnspan=2, padx=10, pady=10)

ttk.Button(app, text="Calculate", command=calculate_gpm).grid(column=0, row=3, columnspan=2, padx=10, pady=10)

app.mainloop()
