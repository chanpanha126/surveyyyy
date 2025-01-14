
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
import sqlite3

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,messagebox


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/chanpanha/Desktop/survey/build/assets/frame6")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

#bacxk to home 

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
    680.0,
    75.0,
    image=image_image_1
)
def gui1():
    window.destroy()
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
    x=451.0,
    y=648.0,
    width=373.0,
    height=76.0
)

canvas.create_text(
    12.0,
    180.0,
    anchor="nw",
    text="Patient Name*",
    fill="#000000",
    font=("Inter Bold", 20 * -1)
)

canvas.create_text(
    9.0,
    325.0,
    anchor="nw",
    text="Date of Birth*",
    fill="#000000",
    font=("Inter", 20 * -1)
)

canvas.create_text(
    12.0,
    484.0,
    anchor="nw",
    text="Medical History*",
    fill="#000000",
    font=("Inter", 20 * -1)
)

canvas.create_text(
    784.0,
    331.0,
    anchor="nw",
    text="Contact Information*",
    fill="#000000",
    font=("Inter", 20 * -1)
)

canvas.create_text(
    774.0,
    484.0,
    anchor="nw",
    text="Assigned Doctor*",
    fill="#000000",
    font=("Inter", 20 * -1)
)

canvas.create_text(
    735.0,
    179.0,
    anchor="nw",
    text="Patient ID*",
    fill="#000000",
    font=("Inter Bold", 20 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    1039.5,
    240.0,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=800.0,
    y=207.0,
    width=479.0,
    height=64.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    297.5,
    240.0,
    image=entry_image_2
)
entry_2 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=58.0,
    y=207.0,
    width=479.0,
    height=64.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    297.5,
    387.0,
    image=entry_image_3
)
entry_3 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=58.0,
    y=354.0,
    width=479.0,
    height=64.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    1046.5,
    393.0,
    image=entry_image_4
)
entry_4 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=807.0,
    y=360.0,
    width=479.0,
    height=64.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    1046.5,
    547.0,
    image=entry_image_5
)
entry_5 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=807.0,
    y=514.0,
    width=479.0,
    height=64.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    297.5,
    547.0,
    image=entry_image_6
)
entry_6 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=58.0,
    y=514.0,
    width=479.0,
    height=64.0
)
def create_database():
    try:
        conn = sqlite3.connect("add_patient.db")
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS add_patient_info (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_name TEXT,
                date_of_birth TEXT,
                medical_history TEXT,
                patient_id TEXT,
                contact_information TEXT,
                assigned_doctor TEXT
            )
        ''')
        conn.commit()
        conn.close()
        print("Database and table created successfully!")
    except sqlite3.Error as e:
        print(f"Error creating database or table: {e}")

create_database()  

# Modified open_home function
def insert_patient_info():
    try:
        conn = sqlite3.connect("add_patient.db")
        cursor = conn.cursor()

        # Get data from the entry widgets (Explicitly convert to strings)
        patient_name = str(entry_2.get("1.0", "end-1c"))
        date_of_birth = str(entry_3.get("1.0", "end-1c"))
        medical_history = str(entry_6.get("1.0", "end-1c"))
        patient_id = str(entry_1.get("1.0", "end-1c"))
        contact_information = str(entry_4.get("1.0", "end-1c"))
        assigned_doctor = str(entry_5.get("1.0", "end-1c"))

        # Insert data into the database
        cursor.execute('''
            INSERT INTO add_patient_info (patient_name, date_of_birth, medical_history, patient_id, contact_information, assigned_doctor)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (patient_name, date_of_birth, medical_history, patient_id, contact_information, assigned_doctor))

        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Patient information inserted successfully!")
        
        #Destroy the current window and open gui1 (login successful)
        window.destroy()
        import build.gui14 as gui14
        gui14.create_home_window()


    except sqlite3.Error as e:
        messagebox.showerror("Error", "Failed to insert patient information.")
button_1.config(command=insert_patient_info)
window.resizable(False, False)
window.mainloop()
