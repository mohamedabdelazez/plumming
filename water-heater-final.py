import tkinter as tk
from tkinter import ttk

# Data from the ASPE table
aspe_data = {
    "Apartment": {
        "Basins, private lavatory": 2,
        "Basins, public lavatory": 20,
        "Bathtubs": 20,
        "Dishwashers": 15,
        "Foot basins": 3,
        "Kitchen sink": 10,
        "Laundry, stationary tubs": 20,
        "Pantry sink": 5,
        "Showers": 30,
        "Service sink": 20,
    },
    "Club": {
        "Basins, private lavatory": 2,
        "Basins, public lavatory": 6,
        "Bathtubs": 20,
        "Dishwashers": 50,
        "Foot basins": 3,
        "Kitchen sink": 20,
        "Laundry, stationary tubs": 28,
        "Pantry sink": 10,
        "Showers": 150,
        "Service sink": 20,
    },
    "Gymnasium": {
        "Basins, private lavatory": 2,
        "Basins, public lavatory": 8,
        "Bathtubs": 30,
        "Foot basins": 12,
        "Showers": 225,
        
    },
    "Hospital": {
        "Basins, private lavatory": 2,
        "Basins, public lavatory": 6,
        "Bathtubs": 20,
        "Dishwashers": 50,
        "Foot basins": 3,
        "Kitchen sink": 20,
        "Laundry, stationary tubs": 28,
        "Pantry sink": 10,
        "Showers": 75,
        "Service sink": 20,
        "Hydrotherapeutic showers": 400,
        "Hubbard baths": 600,
        "Leg baths": 100,
        "Arm baths": 35,
        "Sitz baths": 30,
        "Continuous-flow baths": 165,
        "Circular wash sinks": 20,
        "Semicircular wash sinks": 10,
    },
    "Hotel": {
        "Basins, private lavatory": 2,
        "Basins, public lavatory": 8,
        "Bathtubs": 20,
        "Dishwashers": 50,
        "Foot basins": 3,
        "Kitchen sink": 30,
        "Laundry, stationary tubs": 28,
        "Pantry sink": 10,
        "Showers": 75,
        "Service sink": 30,
        "Circular wash sinks": 20,
        "Semicircular wash sinks": 10,
    },
    "Industrial Plant": {
        "Basins, private lavatory": 2,
        "Basins, public lavatory": 12,
        "Dishwashers": 20,
        "Foot basins": 12,
        "Kitchen sink": 20,
        "Showers": 225,
        "Service sink": 20,
        "Circular wash sinks": 30,
        "Semicircular wash sinks": 10,
    },
    "Office": {
        "Basins, private lavatory": 2,
        "Basins, public lavatory": 6,
        "Bathtubs": 20,
        "Kitchen sink": 20,
        "Laundry, stationary tubs": 20,
        "Pantry sink": 10,
        "Showers": 30,
        "Service sink": 20,
        "Circular wash sinks": 20,
        "Semicircular wash sinks": 10,
    },
    "Private Residence": {
        "Basins, private lavatory": 2,
        "Dishwashers": 15,
        "Foot basins": 3,
        "Kitchen sink": 10,
        "Pantry sink": 5,
        "Showers": 30,
        "Service sink": 15,

    },
    "School": {
        "Basins, private lavatory": 2,
        "Basins, public lavatory": 15,
        "Bathtubs": 30,
        "Dishwashers": 20,
        "Foot basins": 3,
        "Kitchen sink": 20,
        "Laundry, stationary tubs": 28,
        "Pantry sink": 10,
        "Showers": 225,
        "Service sink": 20,
        "Circular wash sinks": 30,
        "Semicircular wash sinks": 15,
    },
    "YMCA": {
        "Basins, private lavatory": 2,
        "Basins, public lavatory": 8,
        "Dishwashers": 20,
        "Foot basins": 12,
        "Kitchen sink": 20,
        "Pantry sink": 10,
        "Showers": 225,
        "Service sink": 20,
    },
}

demand_factors = {
    "Apartment": 0.30,
    "Club": 0.30,
    "Gymnasium": 0.30,
    "Hospital": 0.50,
    "Hotel": 0.40,
    "Industrial Plant": 0.30,
    "Office": 0.20,
    "Private Residence": 0.40,
    "School": 1.00,
    "YMCA": 0.40,
}

storage_capacity_factors = {
    "Apartment": 1.25,
    "Club": 0.90,
    "Gymnasium": 0.90,
    "Hospital": 1.00,
    "Hotel": 1.25,
    "Industrial Plant": 1.00,
    "Office": 0.90,
    "Private Residence": 0.90,
    "School": 2.00,
    "YMCA": 1.00,
}

efficiency_factors = {
    "Electric 95%": 0.95,
    "Gas 80%": 0.80,
    "Steam or Hot Water 85%": 0.85,
    "Custom": None,  # Add a custom option
}

# Initialize the main window
root = tk.Tk()
root.title("Water Heater Capacity")

# Application type dropdown
app_label = tk.Label(root, text="Select Application Type:")
app_label.grid(row=0, column=0, padx=10, pady=10)
app_type = tk.StringVar()
app_dropdown = ttk.Combobox(root, textvariable=app_type, values=list(aspe_data.keys()))
app_dropdown.grid(row=0, column=1, padx=10, pady=10)

# Fixture type dropdown
fixture_label = tk.Label(root, text="Select Fixture:")
fixture_label.grid(row=1, column=0, padx=10, pady=10)
fixture_type = tk.StringVar()
fixture_values = list(aspe_data["Apartment"].keys()) + ["Custom"]
fixture_dropdown = ttk.Combobox(root, textvariable=fixture_type, values=fixture_values, width=22)
fixture_dropdown.grid(row=1, column=1, padx=10, pady=10)


# Custom GPH entry (disabled by default)
custom_gph_label = tk.Label(root, text="Custom GPH:")
custom_gph_label.grid(row=2, column=0, padx=10, pady=10)
custom_gph_entry = tk.Entry(root, state="disabled")
custom_gph_entry.grid(row=2, column=1, padx=10, pady=10)

# Number of fixtures entry
num_label = tk.Label(root, text="Number of Fixtures:")
num_label.grid(row=3, column=0, padx=10, pady=10)
num_fixtures = tk.Entry(root)
num_fixtures.grid(row=3, column=1, padx=10, pady=10)

# Heat source efficiency dropdown
heat_label = tk.Label(root, text="Select Heat Source:")
heat_label.grid(row=4, column=0, padx=10, pady=10)
heat_source = tk.StringVar()
heat_values = list(efficiency_factors.keys())
heat_dropdown = ttk.Combobox(root, textvariable=heat_source, values=heat_values)
heat_dropdown.grid(row=4, column=1, padx=10, pady=10)

# Custom efficiency entry (disabled by default)
custom_efficiency_label = tk.Label(root, text="Custom Efficiency(max 1 ):")
custom_efficiency_label.grid(row=5, column=0, padx=10, pady=10)
custom_efficiency_entry = tk.Entry(root, state="disabled")
custom_efficiency_entry.grid(row=5, column=1, padx=10, pady=10)

# Inlet temperature entry
tin_label = tk.Label(root, text="Inlet Temperature (F):")
tin_label.grid(row=6, column=0, padx=10, pady=10)
tin_entry = tk.Entry(root)
tin_entry.grid(row=6, column=1, padx=10, pady=10)

# Outlet temperature entry
tout_label = tk.Label(root, text="Outlet Temperature (F):")
tout_label.grid(row=7, column=0, padx=10, pady=10)
tout_entry = tk.Entry(root)
tout_entry.grid(row=7, column=1, padx=10, pady=10)

# Result display
result_label = tk.Label(root, text="", fg="blue")
result_label.grid(row=9, columnspan=2, padx=10, pady=10)

# Heater capacity display
heater_capacity_label = tk.Label(root, text="", fg="red")
heater_capacity_label.grid(row=10, columnspan=2, padx=10, pady=10)

# History list
history_label = tk.Label(root, text="History:")
history_label.grid(row=0, column=2, padx=10, pady=10)
history_listbox = tk.Listbox(root, height=20, width=80)
history_listbox.grid(row=1, column=2, rowspan=10, padx=10, pady=10)

# Add buttons to control history
delete_button = tk.Button(root, text="Delete Selected", command=lambda: delete_selected())
delete_button.grid(row=11, column=2, sticky="w", padx=10, pady=5)

clear_button = tk.Button(root, text="Clear All", command=lambda: clear_all())
clear_button.grid(row=11, column=2, sticky="e", padx=10, pady=5)

# Store cumulative GPH and history details
cumulative_gph = 0
history_details = []

# Update fixture dropdown based on application type selection
def update_fixtures(event):
    app = app_type.get()
    if app in aspe_data:
        fixture_values = list(aspe_data[app].keys()) + ["Custom"]
        fixture_dropdown['values'] = fixture_values

app_dropdown.bind("<<ComboboxSelected>>", update_fixtures)

# Enable custom GPH entry if "Custom" is selected
def enable_custom_gph(event):
    if fixture_type.get() == "Custom":
        custom_gph_entry.config(state="normal")
    else:
        custom_gph_entry.config(state="disabled")

fixture_dropdown.bind("<<ComboboxSelected>>", enable_custom_gph)

# Enable custom efficiency entry if "Custom" is selected
def enable_custom_efficiency(event):
    if heat_source.get() == "Custom":
        custom_efficiency_entry.config(state="normal")
    else:
        custom_efficiency_entry.config(state="disabled")

heat_dropdown.bind("<<ComboboxSelected>>", enable_custom_efficiency)

# Function to calculate and display GPH
def calculate():
    global cumulative_gph
    app = app_type.get()
    fixture = fixture_type.get()
    try:
        num = int(num_fixtures.get())
    except ValueError:
        result_label.config(text="Please enter a valid number of fixtures")
        return

    if app and fixture and num > 0:
        if fixture == "Custom":
            try:
                gph_per_fixture = float(custom_gph_entry.get())
            except ValueError:
                result_label.config(text="Please enter a valid custom GPH")
                return
        else:
            gph_per_fixture = aspe_data[app][fixture]

        gph = gph_per_fixture * num
        demand_factor = demand_factors[app]
        storage_capacity_factor = storage_capacity_factors[app]
        cumulative_gph += gph

        result_label.config(text=f"GPH per Fixture: {gph_per_fixture}\n"
                                 f"Demand Factor: {demand_factor}\n"
                                 f"Storage Capacity Factor: {storage_capacity_factor}\n"
                                 f"Total GPH: {cumulative_gph}")

        # Add to history
        history_listbox.insert(tk.END, f"{app} - {fixture}: GPH: {gph}, Total GPH: {cumulative_gph}, "
                                       f"Demand Factor: {demand_factor}, Storage Capacity Factor: {storage_capacity_factor}")
        history_details.append((gph, demand_factor, storage_capacity_factor))
    else:
        result_label.config(text="Please select valid application, fixture, and number of fixtures")

# Function to delete selected history item and update cumulative GPH
def delete_selected():
    global cumulative_gph
    selected_index = history_listbox.curselection()
    if selected_index:
        selected_index = selected_index[0]
        if selected_index < len(history_details):
            gph, _, _ = history_details[selected_index]
            cumulative_gph -= gph
            history_listbox.delete(selected_index)
            del history_details[selected_index]

            # Update result label
            result_label.config(text=f"Total GPH: {cumulative_gph}")
            heater_capacity_label.config(text="")
        else:
            print("Selected index is out of range.")
    else:
        print("No item selected.")

# Function to clear all history and reset cumulative GPH
def clear_all():
    global cumulative_gph
    cumulative_gph = 0
    history_listbox.delete(0, tk.END)
    history_details.clear()

    # Update result label
    result_label.config(text=f"Cumulative GPH: {cumulative_gph}")
    heater_capacity_label.config(text="")

# Function to calculate and display Heater Capacity
def calculate_heater_capacity():
    try:
        tin = float(tin_entry.get())
        tout = float(tout_entry.get())
    except ValueError:
        result_label.config(text="Please enter valid numeric values for Tin and Tout")
        return

    if tin >= tout:
        result_label.config(text="Inlet temperature should be less than outlet temperature")
        return

    heat = heat_source.get()
    if not heat:
        result_label.config(text="Please select a heat source")
        return

    if cumulative_gph == 0:
        result_label.config(text="Please calculate GPH first")
        return

    if heat == "Custom":
        try:
            efficiency = float(custom_efficiency_entry.get())
        except ValueError:
            result_label.config(text="Please enter a valid custom efficiency")
            return
    else:
        efficiency = efficiency_factors[heat]

    gpm = cumulative_gph / 60
    app = app_type.get()
    demand_factor = demand_factors[app]
    storage_capacity_factor = storage_capacity_factors[app]
    
    # Calculate Tank Heater Capacity
    tank_heater_capacity_btu = 500 * gpm * (tout - tin) * demand_factor * storage_capacity_factor / efficiency
    tank_heater_capacity_kw = tank_heater_capacity_btu * 0.00029307107

    # Calculate Instantaneous Heater Capacity
    instantaneous_heater_capacity_btu = 500 * gpm * (tout - tin) / efficiency
     
    instantaneous_heater_capacity_kw = instantaneous_heater_capacity_btu * 0.00029307107

    # Calculate Storage Capacity
    storage_capacity = cumulative_gph * demand_factor * storage_capacity_factor

    heater_capacity_label.config(text=f"Storage Capacity: {storage_capacity:.2f} GPH\n"
                                     f"Tank Heater Capacity: {tank_heater_capacity_btu:.2f} BTU/hr | {tank_heater_capacity_kw:.2f} kW\n"
                                     f"Instantaneous Heater Capacity: {instantaneous_heater_capacity_btu:.2f} BTU/hr | {instantaneous_heater_capacity_kw:.2f} kW")

# Calculate GPH button
calc_button = tk.Button(root, text="Calculate GPH", command=calculate)
calc_button.grid(row=8, column=0, padx=10, pady=10)

# Calculate Heater Capacity button
heater_capacity_button = tk.Button(root, text="Calculate Heater Capacity", command=calculate_heater_capacity)
heater_capacity_button.grid(row=8, column=1, padx=10, pady=10)

# Run the application
root.mainloop()
