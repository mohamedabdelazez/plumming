import tkinter as tk
from tkinter import ttk, messagebox
import math

# Define the fixture_to_sfu dictionary here
fixture_to_sfu = {
    "Bathroom group (Private Flush tank)": {"cold_water": 2.7, "hot_water": 1.5, "total": 3.6},
    "Bathroom group (Private Flush valve)": {"cold_water": 6, "hot_water": 3, "total": 8},
    "Bathtub (Private)": {"cold_water": 1, "hot_water": 1, "total": 1.4},
    "Bathtub (Public)": {"cold_water": 3, "hot_water": 3, "total": 4},
    "Bidet (Private)": {"cold_water": 1.5, "hot_water": 1.5, "total": 2},
    "Combination fixture (Private)": {"cold_water": 2.25, "hot_water": 2.25, "total": 3},
    "Dishwashing machine (Private)": {"cold_water": 0, "hot_water": 1.4, "total": 1.4},
    "Drinking fountain (Offices, etc.)": {"cold_water": 0.25, "hot_water": 0, "total": 0.25},
    "Kitchen sink (Private)": {"cold_water": 1, "hot_water": 1, "total": 1.4},
    "Kitchen sink (Hotel, restaurant)": {"cold_water": 3, "hot_water": 3, "total": 4},
    "Laundry trays(1 to 3) (Private)": {"cold_water": 1, "hot_water": 1, "total": 1.4},
    "Lavatory (Private)": {"cold_water": 0.5, "hot_water": 0.5, "total": 0.7},
    "Lavatory (Public)": {"cold_water": 1.5, "hot_water": 1.5, "total": 2},
    "Service sink (Offices, etc.)": {"cold_water": 2.25, "hot_water": 2.25, "total": 3},
    "Shower head (Public)": {"cold_water": 3, "hot_water": 3, "total": 4},
    "Shower head (Private)": {"cold_water": 1, "hot_water": 1, "total": 1.4},
    "Urinal (Public 1""flush valve)": {"cold_water": 10, "hot_water": 0, "total": 10},
    "Urinal (Public 3/4""flush valve)": {"cold_water": 5, "hot_water": 0, "total": 5},
    "Urinal (Public Flush tank)": {"cold_water": 3, "hot_water": 0, "total": 3},
    "Washing machine (8 lb) (Private)": {"cold_water": 1, "hot_water": 1, "total": 1.4},
    "Washing machine (8 lb) (Public)": {"cold_water": 2.25, "hot_water": 2.25, "total": 3},
    "Washing machine (15 lb) (Public)": {"cold_water": 3, "hot_water": 3, "total": 4},
    "Water closet (Private Flush valve)": {"cold_water": 6, "hot_water": 0, "total": 6},
    "Water closet (Private Flush tank)": {"cold_water": 2.2, "hot_water": 0, "total": 2.2},
    "Water closet (Public Flush valve)": {"cold_water": 10, "hot_water": 0, "total": 10},
    "Water closet (Public Flush tank)": {"cold_water": 5, "hot_water": 0, "total": 5},
    
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

def linear_interpolate(x0, y0, x1, y1, x):
    return y0 + (y1 - y0) * ((x - x0) / (x1 - x0))

def get_gpm(fixture, water_type, flush_mechanism):
    sfu = fixture_to_sfu[fixture][water_type]
    
    if flush_mechanism == "Flush Tank":
        gpm_table = sfu_to_gpm_flush_tank
    elif flush_mechanism == "Flush Valve":
        gpm_table = sfu_to_gpm_flush_valve
    else:
        raise ValueError("Invalid flush mechanism")
    
    if sfu in gpm_table:
        gpm = gpm_table[sfu]
    else:
        # Interpolate if sfu not in the table
        min_sfu, max_sfu = min(gpm_table.keys()), max(gpm_table.keys())
        if sfu < min_sfu:
            gpm = gpm_table[min_sfu]
        elif sfu > max_sfu:
            gpm = gpm_table[max_sfu]
        else:
            min_sfu_gpm, max_sfu_gpm = gpm_table[min_sfu], gpm_table[max_sfu]
            gpm = min_sfu_gpm + ((sfu - min_sfu) / (max_sfu - min_sfu)) * (max_sfu_gpm - min_sfu_gpm)
    
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
fixture_var.set("Water closet (Private Flush valve)")  # default value

water_type_var = tk.StringVar()
water_type_var.set("cold_water")  # default value

flush_mechanism_var = tk.StringVar()
flush_mechanism_var.set("Flush Tank")  # default value

result_var = tk.StringVar()

fixture_label = tk.Label(root, text="Select Fixture:")
fixture_label.pack()

fixture_menu = ttk.Combobox(root, textvariable=fixture_var, width=45)  # Increase the width as needed
fixture_menu['values'] = list(fixture_to_sfu.keys())
fixture_menu.pack()

water_type_menu = ttk.Combobox(root, textvariable=water_type_var, width=45)  # Increase the width as needed
water_type_menu['values'] = ["cold_water", "hot_water", "total"]
water_type_menu.pack()

flush_mechanism_menu = ttk.Combobox(root, textvariable=flush_mechanism_var, width=45)  # Increase the width as needed
flush_mechanism_menu['values'] = ["Flush Tank", "Flush Valve"]
flush_mechanism_menu.pack()


calculate_button = tk.Button(root, text="Calculate", command=calculate_gpm)
calculate_button.pack()

result_label = tk.Label(root, textvariable=result_var)
result_label.pack()

root.mainloop()
