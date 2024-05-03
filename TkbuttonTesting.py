# importing only those functions 
# which are needed 
from tkinter import * 
from tkinter.ttk import *
import customtkinter
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
# creating tkinter window 

root = customtkinter.CTk()
root.title("Button Testing")
root.geometry("500x500")

# Define Images
dots_image = ImageTk.PhotoImage(Image.open("images/dots.png").resize((60, 60), Image.ANTIALIAS))
more_dots_image = ImageTk.PhotoImage(Image.open("images/epic dots epic.png").resize((60, 60), Image.ANTIALIAS))

button1 = customtkinter.CTkButton(master=root, image= dots_image, width=140, height=40, text="dots", compound="left")
button1.pack(pady=20, padx=20)

button2 = customtkinter.CTkButton(master=root, image= more_dots_image, width=140, height=40, text="more dots", compound="right")
button2.pack(pady=20, padx=20)
root.mainloop()