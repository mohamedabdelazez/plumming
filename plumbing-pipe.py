import tkinter as tk
from tkinter import ttk
from fractions import Fraction
import math

# Define the pipe material data
pipe_material_nominal_diameter = {
    "PPR": [Fraction(1, 2), Fraction(3, 4), 1, 1.25, 1.5, 2, 2.5, 3, 4, 6, 8, 10, 12],
    "PVC": [Fraction(1, 2), Fraction(3, 4), 1, 1.25, 1.5, 2, 2.5, 3, 4, 6, 8, 10, 12],
    "HDPE": [Fraction(1, 2), Fraction(3, 4), 1, 1.25, 1.5, 2, 2.5, 3, 4, 6, 8, 10, 12],
}

pipe_material_inner_diameter = {
    "PPR": [0.677, 0.846, 1.146, 1.429, 1.788, 2.252, 2.685, 3.22, 4.472, 5.725, 7.156, 8.948, 11.275],
    "PVC": [0.622, 0.824, 1.049, 1.380, 1.610, 2.067, 2.469, 3.068, 4.026, 5.047, 6.065, 7.981, 10.020],
    "HDPE": [0.622, 0.824, 1.049, 1.380, 1.610, 2.067, 2.469, 3.068, 4.030, 5.050, 6.070, 7.981, 10.020],
}

# Function to calculate velocity in ft/s using inner diameter
def calculate_velocity(flow_rate, inner_diameter):
    # Convert flow rate from gpm to ft^3/s
    flow_rate_ft3s = flow_rate / 448.831
    # Calculate velocity in ft/s
    velocity_fts = flow_rate_ft3s / (math.pi * (inner_diameter/12)**2 / 4)
    return velocity_fts

# Function to calculate head loss using the Darcy-Weisbach equation
def calculate_head_loss(flow_rate, inner_diameter, fluid_density, fluid_viscosity, pipe_length, pipe_material):
    # Convert inner diameter from inches to meters
    inner_diameter_mm = inner_diameter * 25.4
    inner_diameter_m = inner_diameter_mm / 1000
    # Convert flow rate from gpm to m^3/s
    flow_rate_ls = flow_rate * 0.06
    flow_rate_m3s = flow_rate_ls / 1000
    # Calculate pipe area
    pipe_area = (inner_diameter_m ** 2) * math.pi / 4
    # Calculate velocity
    velocity = flow_rate_m3s / pipe_area
    # Calculate Reynolds number
    reynolds_number = velocity * inner_diameter_m * fluid_density / fluid_viscosity
    # Get roughness based on pipe material
    pipe_material_and_roughness = {
        "PPR": 0.007 / 1000,
        "PVC": 0.007 / 1000,
        "HDPE": 0.007 / 1000,
    }
    roughness = pipe_material_and_roughness.get(pipe_material, 0.007 / 1000)
    # Calculate friction factor using Colebrook-White equation
    friction_factor = calculate_friction_factor(inner_diameter_m, reynolds_number, roughness)
    # Calculate head loss
    head_loss = (friction_factor * pipe_length * velocity ** 2) / (2 * 9.81 * inner_diameter_m)
    return head_loss

# Function to calculate friction factor using Colebrook-White equation
def calculate_friction_factor(diameter, reynolds, roughness):
    friction = 0.08  # Starting friction factor
    while True:
        left_f = 1 / friction ** 0.5
        right_f = -2 * math.log10((2.51 / (reynolds * friction ** 0.5)) + (roughness / (3.72 * diameter)))
        if abs(left_f - right_f) < 0.0001:
            break
        friction = friction - 0.000001  # Change friction factor
    return friction

# Function to update diameters in the dropdown based on selected material
def update_diameters(event):
    material = material_var.get()
    diameter_dropdown['values'] = [str(d) for d in pipe_material_nominal_diameter[material]]
    diameter_dropdown.current(0)

# Function to calculate and display the results
def select_pipe():
    material = material_var.get()
    diameter_index = diameter_dropdown.current()
    flow_rate = float(flow_rate_entry.get())
    
    inner_diameter = pipe_material_inner_diameter[material][diameter_index]
    velocity = calculate_velocity(flow_rate, inner_diameter)
    friction_loss = calculate_head_loss(flow_rate, inner_diameter, fluid_density=1000, fluid_viscosity=0.001, pipe_length=100, pipe_material=material)
    
    if velocity > 4:
        result_label.config(text=f"Warning: Velocity exceeds 4 ft/s.\nVelocity: {velocity:.2f} ft/s.\nFriction Loss: {friction_loss:.2f} psi/100ft.\nSelected diameter may not be suitable.")
    else:
        result_label.config(text=f"Velocity: {velocity:.2f} ft/s.\nFriction Loss: {friction_loss:.2f} psi/100ft.\nSelected diameter is suitable.")

# Setting up the GUI
root = tk.Tk()
root.title("Plumbing Pipe Diameter Selector")

material_var = tk.StringVar(value=list(pipe_material_nominal_diameter.keys())[0])
material_dropdown = ttk.Combobox(root, textvariable=material_var, values=list(pipe_material_nominal_diameter.keys()))
material_dropdown.bind("<<ComboboxSelected>>", update_diameters)
material_dropdown.pack(pady=5)

diameter_var = tk.StringVar()
diameter_dropdown = ttk.Combobox(root, textvariable=diameter_var)
update_diameters(None)  # Initialize diameter dropdown
diameter_dropdown.pack(pady=5)

flow_rate_label = tk.Label(root, text="Flow Rate (GPM):")
flow_rate_label.pack()
flow_rate_entry = tk.Entry(root)
flow_rate_entry.pack(pady=5)

select_button = tk.Button(root, text="Select Pipe", command=select_pipe)
select_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
