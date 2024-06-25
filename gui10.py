
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

import sqlite3
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/chanpanha/Desktop/survey/build/assets/frame10")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1366x768")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 768,
    width = 1366,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    672.3502807617188,
    74.668212890625,
    image=image_image_1
)

canvas.create_text(
    138.0,
    128.0,
    anchor="nw",
    text="Name*",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    128.0,
    266.0,
    anchor="nw",
    text="ID's Appointment *",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    116.0,
    403.0,
    anchor="nw",
    text="Doctor Name *",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    116.0,
    520.0,
    anchor="nw",
    text="Date and Time*",
    fill="#000000",
    font=("Inter", 24 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    720.5,
    197.0,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=149.0,
    y=164.0,
    width=1143.0,
    height=64.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    712.0,
    337.5,
    image=entry_image_2
)
entry_2 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=132.5,
    y=304.0,
    width=1159.0,
    height=65.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    712.0,
    475.0,
    image=entry_image_3
)
entry_3 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=132.0,
    y=442.0,
    width=1160.0,
    height=64.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    713.5,
    591.5,
    image=entry_image_4
)
entry_4 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=135.5,
    y=558.0,
    width=1156.0,
    height=65.0
)
def gui1():
    window.destroy()
    import gui1
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=gui1,
    relief="flat"
)
button_1.place(
    x=534.0,
    y=675.0,
    width=373.0,
    height=76.0
)
def create_database():
    try:
        conn = sqlite3.connect("add_appointment.db")  # Changed database name
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS add_appointment_info (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                email_address TEXT,
                doctor_name TEXT,
                date_time TEXT 
            )
        ''')  # Changed table name and columns
        conn.commit()
        conn.close()
        print("Database and table created successfully!")
    except sqlite3.Error as e:
        print(f"Error creating database or table: {e}")

create_database()  # Call the function to create the database and table

def insert_appointment_info():
    try:
        conn = sqlite3.connect("add_appointment.db")
        cursor = conn.cursor()

        # Get data from the entry widgets (Explicitly convert to strings)
        name = str(entry_1.get("1.0", "end-1c"))
        email_address = str(entry_2.get("1.0", "end-1c"))
        doctor_name = str(entry_3.get("1.0", "end-1c"))
        date_time = str(entry_4.get("1.0", "end-1c"))

        # Insert data into the database
        cursor.execute('''
            INSERT INTO add_appointment_info (name, email_address, doctor_name, date_time)
            VALUES (?, ?, ?, ?)
        ''', (name, email_address, doctor_name, date_time))

        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Appointment information inserted successfully!")

        # Destroy the current window and open gui1 (login successful)
        window.destroy()
        import build.gui14 as gui14
        gui14.create_home_window()
    except sqlite3.Error as e:
      
        messagebox.showerror("Error", "Failed to insert appointment information.")

button_1.config(command=insert_appointment_info)
window.resizable(False, False)
window.mainloop()