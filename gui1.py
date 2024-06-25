
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/chanpanha/Desktop/Survey/build/assets/frame1")


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
canvas.create_text(
    683.0,
    237.0,
    anchor="nw",
    text="MALCETTE",
    fill="#000000",
    font=("Inter", 96 * -1)
)

canvas.create_text(
    950.0,
    353.0,
    anchor="nw",
    text="Hospital ",
    fill="#000000",
    font=("Inter", 64 * -1)
)
def gui2():
    window.destroy()
    import gui2
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=gui2,
    relief="flat"
)
button_1.place(
    x=125.0,
    y=85.0,
    width=200.0,
    height=69.0
)
def gui5():
    window.destroy()
    import gui5
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=gui5,
    relief="flat"
)
button_2.place(
    x=121.0,
    y=209.0,
    width=200.0,
    height=69.0
)
def gui10():
    window.destroy()
    import gui10
button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=gui10,
    relief="flat"
)
button_3.place(
    x=121.0,
    y=334.0,
    width=200.0,
    height=69.0
)

canvas.create_text(
    144.0,
    309.0,
    anchor="nw",
    text="Book Appointment",
    fill="#000000",
    font=("Inter SemiBold", 16 * -1)
)
def gui11():
    window.destroy()
    import gui11
button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=gui11,
    relief="flat"
)
button_4.place(
    x=121.0,
    y=464.0,
    width=200.0,
    height=69.0
)

canvas.create_text(
    137.0,
    442.0,
    anchor="nw",
    text="Cancel Appointment",
    fill="#000000",
    font=("Inter SemiBold", 16 * -1)
)
def gui12():
    window.destroy()
    import gui12
button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=gui12,
    relief="flat"
)
button_5.place(
    x=121.0,
    y=603.0,
    width=200.0,
    height=69.0
)
button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=121.0,
    y=764.0,
    width=200.0,
    height=69.0
)

canvas.create_text(
    126.0,
    58.0,
    anchor="nw",
    text="Insert Doctor Information",
    fill="#000000",
    font=("Inter SemiBold", 16 * -1)
)

canvas.create_text(
    122.0,
    186.0,
    anchor="nw",
    text="Patient’s Information",
    fill="#000000",
    font=("Inter SemiBold", 16 * -1)
)

canvas.create_text(
    137.0,
    564.0,
    anchor="nw",
    text="Reschedule Appointment",
    fill="#000000",
    font=("Inter SemiBold", 16 * -1)
)

canvas.create_text(
    144.0,
    791.0,
    anchor="nw",
    text="Change Password",
    fill="#000000",
    font=("Inter SemiBold", 16 * -1)
)
window.resizable(False, False)
window.mainloop()