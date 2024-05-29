import tkinter as tk
from tkinter import ttk, messagebox

# Define the fixture_to_sfu dictionary here
fixture_to_sfu = {
    "Fixture A": {"cold_water": 5, "hot_water": 8, "total": 12},
    "Fixture B": {"cold_water": 6, "hot_water": 9, "total": 13},
    "Fixture C": {"cold_water": 7, "hot_water": 10, "total": 15}
    # Add more fixtures as needed
}

def linear_interpolate(x0, y0, x1, y1, x):
    return y0 + (y1 - y0) * ((x - x0) / (x1 - x0))

def get_gpm(fixture, water_type, flush_mechanism):
    # Plumbing fixture to SFU mappings
    fixture_to_sfu = {
        "Fixture A": {"cold_water": 5, "hot_water": 8, "total": 12},
        "Fixture B": {"cold_water": 6, "hot_water": 9, "total": 13},
        "Fixture C": {"cold_water": 7, "hot_water": 10, "total": 15}
        # Add more fixtures as needed
    }

    # SFU to GPM conversion tables based on IPC standards
    sfu_to_gpm_flush_tank = {
        1: 3, 2: 5, 3: 6.5, 4: 8, 5: 9.4, 6: 10.7, 7: 11.8, 8: 12.8, 9: 13.7, 10: 14.6,
        11: 15.4, 12: 16, 13: 16.5, 14: 17, 15: 17.5, 16: 18, 17: 18.4, 18: 18.8, 19: 19.2,
        20: 19.6, 25: 21.5, 30: 23.3, 35: 24.9, 40: 26.3, 45: 27.7, 50: 29.1, 60: 32, 70: 35,
        80: 38, 90: 41, 100: 43.5, 120: 48, 140: 52.5, 160: 57, 180: 61, 200: 65, 225: 70,
        250: 75, 275: 80, 300: 85, 400: 105, 500: 124, 750: 170, 1000: 208, 1250: 239,
        1500: 269, 1750: 297, 2000: 325, 2500: 380, 3000: 433, 4000: 535, 5000: 593
    }

    sfu_to_gpm_flush_valve = {
        5: 15, 6: 17.4, 7: 19.8, 8: 22.2, 9: 24.6, 10: 27, 11: 27.8, 12: 28.6, 13: 29.4, 14: 30.2,
        15: 31, 16:31.8, 17: 32.6, 18: 33.4, 19: 34.2, 20: 35, 25: 38.5, 30: 42, 35: 45.5,
        40: 49, 45: 52.5, 50: 56, 60: 62, 70: 68, 80: 74, 90: 80, 100: 86, 120: 96, 140: 106,
        160: 116, 180: 126, 200: 136, 225: 146, 250: 156, 275: 166, 300: 176, 400: 206, 500: 236,
        750: 286, 1000: 336, 1250: 386, 1500: 436, 1750: 486, 2000: 536, 2500: 636, 3000: 736,
        4000: 936, 5000: 1136
    }

    # Calculate GPM based on the selected fixture, water type, and flush mechanism
    if flush_mechanism == "Tank":
        sfu = fixture_to_sfu[fixture][water_type]
        gpm = linear_interpolate(1, 3, 1000, 208, sfu)
    elif flush_mechanism == "Valve":
        sfu = fixture_to_sfu[fixture][water_type]
        gpm = linear_interpolate(5, 15, 5000, 593, sfu)

    return gpm

def calculate_gpm():
    fixture = fixture_var.get()
    water_type = water_type_var.get()
    flush_mechanism = flush_mechanism_var.get()
    gpm = get_gpm(fixture, water_type, flush_mechanism)
    result_var.set(f"WSFU: {fixture_to_sfu[fixture][water_type]} | GPM: {gpm:.2f}")

root = tk.Tk()
root.title("Plumbing Fixture GPM Calculator")

fixture_var = tk.StringVar()
fixture_var.set("Fixture A")  # default value

water_type_var = tk.StringVar()
water_type_var.set("cold_water")  # default value

flush_mechanism_var = tk.StringVar()
flush_mechanism_var.set("Tank")  # default value

result_var = tk.StringVar()

fixture_label = tk.Label(root, text="Select Fixture:")
fixture_label.pack()

fixture_menu = ttk.Combobox(root, textvariable=fixture_var)
fixture_menu['values'] = list(fixture_to_sfu.keys())
fixture_menu.pack()

water_type_label = tk.Label(root, text="Select Water Type:")
water_type_label.pack()

water_type_menu = ttk.Combobox(root, textvariable=water_type_var)
water_type_menu['values'] = ["cold_water", "hot_water", "total"]
water_type_menu.pack()

flush_mechanism_label = tk.Label(root, text="Select Flush Mechanism:")
flush_mechanism_label.pack()

flush_mechanism_menu = ttk.Combobox(root, textvariable=flush_mechanism_var)
flush_mechanism_menu['values'] = ["Tank", "Valve"]
flush_mechanism_menu.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate_gpm)
calculate_button.pack()

result_label = tk.Label(root, textvariable=result_var)
result_label.pack()

root.mainloop()
