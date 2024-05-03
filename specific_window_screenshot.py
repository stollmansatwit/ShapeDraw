import pygetwindow
import pyautogui
from PIL import Image
import time
from customtkinter import *
import datetime
from dateutil.relativedelta import relativedelta

now = datetime.datetime.now()
date_formated = now.strftime("%m-%d-%Y")


#Mini Window
root = CTk()
root.title("Screenshot Window")
root.geometry("300x300")
set_appearance_mode("Dark")




titles = pygetwindow.getAllTitles()
newtitles = []
for i in range(1, len(titles)):
    if len(titles[i-1]) > 1:
        newtitles.append(titles[i-1])

#Dropdown grabs all the window titles with names
dropdown = CTkComboBox(master=root, values=newtitles, fg_color="black", dropdown_fg_color="black", text_color="white", corner_radius=10, width=200, height=50, font=("Arial", 20))
dropdown.place(relx=0.5, rely=0.25, anchor="center")



def screenshot():
    path = 'images\\' + dropdown.get() + date_formated + '-Screenshot.png'
    window = pygetwindow.getWindowsWithTitle(dropdown.get())[0]
    window.activate()

    left, top = window.topleft
    right, bottom = window.bottomright
    pyautogui.screenshot(path)
    im = Image.open(path)
    im = im.crop((left+10, top+10, right-10, bottom-10))
    
    im.save(path)
    im.show(path)
    label2.place(relx=0.5, rely=0.9, anchor="center")

#     greenFilter(im)
#     im.show(path)

# def greenFilter(img):
#     for x in range(img.width):
#        for y in range(img.height):
#            r, g, b = img.getpixel((x, y))
#            if g > 100:
#                img.putpixel((x, y), (0, 255, 0))
#     return img

#label 
label = CTkLabel(master=root, text="Select a window to screenshot:", fg_color="transparent", text_color="white", font=("Arial", 20))
label.place(relx=0.5, rely=0.05, anchor="center")

label2 = CTkLabel(master=root, text="Screenshot saved to images folder", fg_color="transparent", text_color="white", font=("Arial", 15))
#Create button
button = CTkButton(master=root, text="Screenshot", fg_color="black", command=screenshot, text_color="white", width=200, height=100, font=("Arial", 40), corner_radius=55, hover_color="red")
button.place(relx=0.5, rely=0.6, anchor="center")

root.mainloop()