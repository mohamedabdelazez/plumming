import tkinter as tk
from tkinter import ttk, messagebox

def linear_interpolate(x0, y0, x1, y1, x):
    return y0 + (y1 - y0) * ((x - x0) / (x1 - x0))

def get_gpm(sfu, flush_mechanism):
    sfu_to_gpm_flush_tank = {
        1: 3, 2: 5, 3: 6.5, 4: 8, 5: 9.4, 6: 10.7, 7: 11.8, 8: 12.8, 9: 13.7, 10: 14.6,
        11: 15.4, 12: 16, 13: 16.5, 14: 17, 15: 17.5, 16: 18, 17: 18.4, 18: 18.8, 19: 19.2,
        20: 19.6, 25: 21.5, 30: 23.3, 35: 24.9, 40: 26.3, 45: 27.7, 50: 29.1, 60: 32,
        70: 35, 80: 38, 90: 41, 100: 43.5, 120: 48, 140: 52.5, 160: 57, 180: 61, 200: 65,
        225: 70, 250: 75, 275: 80, 300: 85, 400: 105, 500: 124, 750: 170, 1000: 208,
        1250: 239, 1500: 269, 1750: 297, 2000: 325, 2500: 380, 3000: 433, 4000: 535,
        5000: 593
    }

    sfu_to_gpm_flush_valve = {
        5: 15, 6: 17.4, 7: 19.8, 8: 22.2, 9: 24.6, 10: 27, 11: 27.8, 12: 28.6, 13: 29.4, 14: 30.2,
        15: 31, 16: 31.8, 17: 32.6, 18: 33.4, 19: 34.2, 20: 35, 25: 38.5, 30: 42, 35: 45.5,
        40: 49, 45: 52.5, 50: 56, 60: 62, 70: 68, 80: 74, 90: 80, 100: 86, 120: 96, 140: 106,
        160: 116, 180: 126, 200: 136, 225: 146, 250: 156, 275: 166, 300: 176, 400: 206,
        500: 236, 750: 286, 1000: 336, 1250: 386, 1500: 436, 1750: 486, 2000: 536,
        2500: 636, 3000: 736, 4000: 936, 5000: 1136
    }

    if flush_mechanism == "flush_tank":
        conversion_table = sfu_to_gpm_flush_tank
    elif flush_mechanism == "flush_valve":
        conversion_table = sfu_to_gpm_flush_valve
    else:
        raise ValueError("Invalid flush mechanism type")

    min_sfu = min(conversion_table.keys())
    max_sfu = max(conversion_table.keys())

    if sfu < min_sfu:
        messagebox.showinfo("Notice", f"The lowest WSFU value according to IPC is {min_sfu}.")
        return conversion_table[min_sfu]
    elif sfu > max_sfu:
        messagebox.showerror("Error", "WSFU value is out of range")
        return None
    elif sfu in conversion_table:
        return conversion_table[sfu]
    else:
        sorted_keys = sorted(conversion_table.keys())
        for i in range(len(sorted_keys) - 1):
            if sorted_keys[i] < sfu < sorted_keys[i + 1]:
                x0, y0 = sorted_keys[i], conversion_table[sorted_keys[i]]
                x1, y1 = sorted_keys[i + 1], conversion_table[sorted_keys[i + 1]]
                return linear_interpolate(x0, y0, x1, y1, sfu)

def calculate_gpm():
    try:
        sfu = float(sfu_var.get())
        flush_mechanism = flush_mechanism_var.get()
        gpm = get_gpm(sfu, flush_mechanism)
        if gpm is not None:
            result_var.set(f"GPM: {gpm:.2f}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

app = tk.Tk()
app.title("Plumbing GPM Calculator")

# Apply a modern theme
style = ttk.Style(app)
style.theme_use('clam')

# Configure styles
style.configure('TLabel', font=('Helvetica', 12), padding=10)
style.configure('TButton', font=('Helvetica', 12), padding=10)
style.configure('TEntry', font=('Helvetica', 12), padding=10)
style.configure('TCombobox', font=('Helvetica', 12), padding=10)

# Colors and padding
app.configure(bg='#f2f2f2')

frame = ttk.Frame(app, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(frame, text="WSFU:").grid(column=0, row=0, padx=10, pady=10, sticky=tk.E)
sfu_var = tk.StringVar()
ttk.Entry(frame, textvariable=sfu_var).grid(column=1, row=0, padx=10, pady=10)

ttk.Label(frame, text="Flush Mechanism:").grid(column=0, row=1, padx=10, pady=10, sticky=tk.E)
flush_mechanism_var = tk.StringVar(value="flush_tank")
flush_mechanism_combobox = ttk.Combobox(frame, textvariable=flush_mechanism_var, values=["flush_tank", "flush_valve"])
flush_mechanism_combobox.grid(column=1, row=1, padx=10, pady=10)

result_var = tk.StringVar()
ttk.Label(frame, textvariable=result_var, foreground="#007700", font=("Helvetica", 14)).grid(column=0, row=2, columnspan=2, padx=10, pady=10)

ttk.Button(frame, text="Calculate", command=calculate_gpm).grid(column=0, row=3, columnspan=2, padx=10, pady=10)

for widget in frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

app.mainloop()
