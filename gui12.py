
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,messagebox
import sqlite3
import sys

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/chanpanha/Desktop/survey/build/assets/frame12")


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
    714.0,
    83.0,
    image=image_image_1
)

canvas.create_text(
    274.0,
    169.0,
    anchor="nw",
    text=" Appointment ID *",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    249.0,
    291.0,
    anchor="nw",
    text=" Appointment Old Date *",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    247.0,
    401.0,
    anchor="nw",
    text=" Appointment New Date *",
    fill="#000000",
    font=("Inter", 24 * -1)
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
    x=458.0,
    y=660.0,
    width=449.0,
    height=74.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    664.5,
    243.5,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=306.5,
    y=211.0,
    width=716.0,
    height=63.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    664.5,
    359.5,
    image=entry_image_3
)
entry_3 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=306.5,
    y=327.0,
    width=716.0,
    height=63.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    664.5,
    471.5,
    image=entry_image_4
)
entry_4 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=306.5,
    y=439.0,
    width=716.0,
    height=63.0
)

def update_appointment_info():
    try:
        conn = sqlite3.connect("add_appointment.db")
        cursor = conn.cursor()

        # Get data from the entry widgets
        appointment_id = entry_1.get("1.0", "end-1c").strip()
        old_date = entry_3.get("1.0", "end-1c").strip() 
        new_date = entry_4.get("1.0", "end-1c").strip()

        # Check if appointment_id and new_date are provided
        if appointment_id and new_date:
            # Update the appointment
            cursor.execute("""
                UPDATE add_appointment_info 
                SET date_time = ?, reason = ? 
                WHERE id = ? AND date_time = ?
            """, (new_date, reason, appointment_id, old_date)) 

            conn.commit()  

            if cursor.rowcount > 0:  
                messagebox.showinfo("Success", "Appointment rescheduled successfully!")
            else:
                messagebox.showinfo("Not Found", "No appointment with that ID and old date found.")
        else:
            messagebox.showerror("Error", "Please enter Appointment ID, old date, and new date.")

        conn.close()

    except sqlite3.Error as e:
        print(f"Error updating appointment: {e}")
        messagebox.showerror("Error", f"Database error: {e}")
button_1.config(command=update_appointment_info)
window.resizable(False, False)
window.mainloop()
