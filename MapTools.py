import customtkinter
import tkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.title("Map Tools v0.1 | by Shtakelberg")
app.geometry("1000x500+500+300")

coords = ""

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

#label2 = customtkinter.CTkLabel(app, text="playsound cmd", fg_color="transparent")
#label2.place(relx=0.48, rely=0.1, anchor=tkinter.CENTER)



app.mainloop()