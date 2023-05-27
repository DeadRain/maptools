from asyncio.windows_events import NULL
from multiprocessing import Value
import customtkinter
import tkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.title("Map Tools v0.2 | by Shtakelberg")
app.geometry("1000x500+500+300")

coords = ""
type = "ambient"
volume = 50

def button_function1():
    global coords
    coords = entry.get()
    button_function()

def button_function():
    global coords
    splitted = coords.split(" ")
    getIn = 'execute if entity @a[x={},y={},z={},dx=0] run function {}'

    if len(splitted) != 3:
        dialog = customtkinter.CTkInputDialog(text="Incorrect data. Enter the correct:", title="Editing cords")
        coords = dialog.get_input()
        button_function()
        return
    
    if (check_var.get() == "on"):
        app.clipboard_clear()
        app.clipboard_append(getIn.format(splitted[0],splitted[1],splitted[2],entry2.get()))

    print(getIn.format(splitted[0],splitted[1],splitted[2],entry2.get()))

def button_function2():
    global type
    global volume

    getIn = 'playsound {} {} {} {} {} 1'

    soundName = entry3.get()
    type_ = type
    selector = entry5.get()
    coord = entry4.get()
    vol = volume

    app.clipboard_clear()
    app.clipboard_append(getIn.format(soundName, type_, selector, coord, vol))

    print(getIn.format(soundName, type_, selector, coord, vol))

def combobox_callback(choice):
    global type
    type = choice
    print("combobox dropdown clicked:", choice)

def slider_event(value):

    global volume
    volume = int(value)
    print(value)
    label2.configure(text="Громкость: " + str(value))

#execute if entity...
label = customtkinter.CTkLabel(app, text="if entity cmd", fg_color="transparent")
label.place(relx=0.18, rely=0.1, anchor=tkinter.CENTER)

entry = customtkinter.CTkEntry(app, placeholder_text="coordinates")
entry2 = customtkinter.CTkEntry(app, placeholder_text="function")

entry.place(relx=0.1, rely=0.15, anchor=tkinter.CENTER)
entry2.place(relx=0.25, rely=0.15, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app, text="Generate", command=button_function1)
button.place(relx=0.1, rely=0.22, anchor=tkinter.CENTER)

check_var = customtkinter.StringVar(value="off")
checkbox = customtkinter.CTkCheckBox(app, text="Copy to clipboard", variable=check_var, onvalue="on", offvalue="off")
checkbox.place(relx=0.25, rely=0.22, anchor=tkinter.CENTER)

#playsound...

label2 = customtkinter.CTkLabel(app, text="playsound cmd", fg_color="transparent")
label2.place(relx=0.48, rely=0.1, anchor=tkinter.CENTER)

entry3 = customtkinter.CTkEntry(app, placeholder_text="sound name")

combobox = customtkinter.CTkComboBox(app, values=["ambient", "block", "hostile", "master", "music", "neutral", "player", "record", "voice", "weather"],
                                     command=combobox_callback)

entry4 = customtkinter.CTkEntry(app, placeholder_text="~ ~ ~")

slider = customtkinter.CTkSlider(app, from_=0, to=100, number_of_steps=10, width=100, command=slider_event)

entry5 = customtkinter.CTkEntry(app, placeholder_text="selector")

button = customtkinter.CTkButton(master=app, text="Generate", width=300, command=button_function2)

entry3.place(relx=0.43, rely=0.15, anchor=tkinter.CENTER)
combobox.place(relx=0.58, rely=0.15, anchor=tkinter.CENTER)
entry4.place(relx=0.73, rely=0.15, anchor=tkinter.CENTER)
slider.place(relx=0.87, rely=0.15, anchor=tkinter.CENTER)

entry5.place(relx=0.43, rely=0.22, anchor=tkinter.CENTER)
button.place(relx=0.66, rely=0.22, anchor=tkinter.CENTER)


app.mainloop()