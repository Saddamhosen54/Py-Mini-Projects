import tkinter as tk
from tkinter import messagebox, filedialog
from tkcalendar import Calendar
from fpdf import FPDF
from datetime import datetime


# Create the main window
root = tk.Tk()
root.title("Hotel Billing System")
root.geometry("700x900")


# Variables for storing user inputs
customer_name = tk.StringVar()
customer_phone = tk.StringVar()
room_price = tk.DoubleVar()
check_in_date = tk.StringVar()
check_out_date = tk.StringVar()
num_days = tk.IntVar(value=1)
advance_payment = tk.DoubleVar(value=0)


# Room types
room_types = ["Single Room", "Double Room", "Suite"]
selected_room = tk.StringVar()
selected_room.set("Select Room Type")


# Services and their prices
service_prices = {
    "Breakfast": 300,
    "Lunch": 500,
    "Dinner": 700,
    "Laundry": 150,
    "Spa": 1000
}


selected_services = {
    "Breakfast": tk.IntVar(),
    "Lunch": tk.IntVar(),
    "Dinner": tk.IntVar(),
    "Laundry": tk.IntVar(),
    "Spa": tk.IntVar()
}

# Function to open the calendar for check-in date
def open_calendar_checkin():
    cal_window = tk.Toplevel(root)
    cal_window.grab_set()
    cal_window.title("Select Check-in Date")
    
    cal = Calendar(cal_window, selectmode="day", date_pattern="dd/mm/yyyy")
    cal.pack(pady=20)

    def select_date():
        check_in_date.set(cal.get_date())
        cal_window.destroy()

    tk.Button(cal_window, text="Select Date", command=select_date).pack(pady=10)

# Function to open the calendar for check-out date
def open_calendar_checkout():
    cal_window = tk.Toplevel(root)
    cal_window.grab_set()
    cal_window.title("Select Check-out Date")
    
    cal = Calendar(cal_window, selectmode="day", date_pattern="dd/mm/yyyy")
    cal.pack(pady=20)

    def select_date():
        check_out_date.set(cal.get_date())
        cal_window.destroy()

    tk.Button(cal_window, text="Select Date", command=select_date).pack(pady=10)

# Function to calculate the total bill
def calculate_bill():
    try:
        # Calculate room cost
        total_room_cost = room_price.get() * num_days.get()
        
        # Calculate service cost
        total_service_cost = sum(service_prices[service] for service, var in selected_services.items() if var.get() == 1)
        
        # Calculate grand total
        total_amount = total_room_cost + total_service_cost
        
        # Calculate due amount after adjusting advance payment
        due_amount = total_amount - advance_payment.get()
        
        # Display the bill summary
        bill_summary = (
            f"Customer Name: {customer_name.get()}\n"
            f"Phone: {customer_phone.get()}\n"
            f"Room Type: {selected_room.get()}\n"
            f"Check-in Date: {check_in_date.get()}\n"
            f"Check-out Date: {check_out_date.get()}\n"
            f"Total Days: {num_days.get()}\n"
            f"Room Charges: {total_room_cost} BDT\n"
            f"Service Charges: {total_service_cost} BDT\n"
            f"Advance Payment: {advance_payment.get()} BDT\n"
            f"Total Bill: {total_amount} BDT\n"
            f"Total Due: {due_amount} BDT"
        )
        messagebox.showinfo("Bill Summary", bill_summary)
        
        # Save the bill as a PDF
        save_bill(total_room_cost, total_service_cost, total_amount, due_amount)
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {e}")

# Function to save the bill as a PDF
def save_bill(room_cost, service_cost, total_cost, due_amount):
    try:
        # File name based on phone number
        save_path = f"{customer_phone.get()}_bill.pdf"
        
        # Create PDF document
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        
        # Add letterhead
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(200, 10, "Hotel Sunshine", 0, 1, 'C')
        pdf.set_font("Arial", '', 12)
        pdf.cell(200, 10, "123 Sunshine Street, Dhaka, Bangladesh", 0, 1, 'C')
        pdf.cell(200, 10, "Phone: +880 123-4567890", 0, 1, 'C')
        pdf.cell(200, 10, "----------------------------------------------", 0, 1, 'C')
        
        # Customer details
        pdf.cell(200, 10, f"Customer Name: {customer_name.get()}", 0, 1)
        pdf.cell(200, 10, f"Phone: {customer_phone.get()}", 0, 1)
        
        # Room details
        pdf.cell(200, 10, f"Room Type: {selected_room.get()}", 0, 1)
        pdf.cell(200, 10, f"Check-in Date: {check_in_date.get()}", 0, 1)
        pdf.cell(200, 10, f"Check-out Date: {check_out_date.get()}", 0, 1)
        pdf.cell(200, 10, f"Total Days: {num_days.get()}", 0, 1)
        pdf.cell(200, 10, f"Room Charges: {room_cost} BDT", 0, 1)
        
        # Service charges
        pdf.cell(200, 10, f"Service Charges: {service_cost} BDT", 0, 1)
        pdf.cell(200, 10, f"Advance Payment: {advance_payment.get()} BDT", 0, 1)
        pdf.cell(200, 10, f"Total Bill: {total_cost} BDT", 0, 1)
        pdf.cell(200, 10, f"Total Due: {due_amount} BDT", 0, 1)
        
        # Save PDF
        pdf.output(save_path)
        messagebox.showinfo("Saved", f"Bill saved successfully as: {save_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Error saving the bill: {e}")

# Create UI Elements
tk.Label(root, text="Hotel Billing System", font=("Arial", 20, "bold")).pack(pady=10)

tk.Label(root, text="Customer Name").pack()
tk.Entry(root, textvariable=customer_name).pack()

tk.Label(root, text="Phone").pack()
tk.Entry(root, textvariable=customer_phone).pack()

tk.Label(root, text="Select Room Type").pack()
room_dropdown = tk.OptionMenu(root, selected_room, *room_types)
room_dropdown.pack()

tk.Label(root, text="Room Price (BDT per day)").pack()
tk.Entry(root, textvariable=room_price).pack()

# Check-in date input with calendar
tk.Label(root, text="Check-in Date").pack()
tk.Button(root, text="Select Check-in Date", command=open_calendar_checkin).pack()
tk.Entry(root, textvariable=check_in_date, state="readonly").pack()

# Check-out date input with calendar
tk.Label(root, text="Check-out Date").pack()
tk.Button(root, text="Select Check-out Date", command=open_calendar_checkout).pack()
tk.Entry(root, textvariable=check_out_date, state="readonly").pack()

tk.Label(root, text="Number of Days").pack()
tk.Entry(root, textvariable=num_days).pack()

tk.Label(root, text="Advance Payment (BDT)").pack()
tk.Entry(root, textvariable=advance_payment).pack()

tk.Label(root, text="Additional Services", font=("Arial", 14)).pack(pady=5)
for service, price in service_prices.items():
    tk.Checkbutton(
        root,
        text=f"{service} ({price} BDT)",
        variable=selected_services[service]
    ).pack(anchor="w")

tk.Button(root, text="Calculate & Save Bill", command=calculate_bill, bg="green", fg="white", font=("Arial", 14)).pack(pady=10)

# Run the main loop
root.mainloop()
