from customtkinter import *
from turtle import *
from tkinter import *
from customtkinter import *
from random import randint
from PIL import Image, ImageTk


# setup(width=1920, height=1080)
screen = Screen()
canvas = screen.cv
# screen.cv._rootwindow.resizable(False, False)
shape("turtle")


#Mini Window
root = CTk()
root.title("Draw Shapes")
root.geometry("300x600")
set_appearance_mode("Light")



#Dropdown menu
options = ["Flower", "Square", "Circle", "Triangle", "Star", "Pentagon", 
           "Hexagon", "Octagon", "Swirl", "Heptagon", "Nonagon", "Decagon"]

# Create a CTkComboBox
dropdown = CTkComboBox(master=root, values=options, fg_color="sky blue")
dropdown.place(relx=0.5, rely=0.07, anchor="center")

def dark_mode_button_func():
    if get_appearance_mode() == "Dark":
        set_appearance_mode("Light")
        label1.configure(text_color="black")
        label2.configure(text_color="black")
        label3.configure(text_color="black")
        label4.configure(text_color="black")
        label5.configure(text_color="black")
        label6.configure(text_color="black")
        label7.configure(text_color="black")
        bgcolor("white")
        
    else:
        set_appearance_mode("Dark")
        label1.configure(text_color="white")
        label2.configure(text_color="white")
        label3.configure(text_color="white")
        label4.configure(text_color="white")
        label5.configure(text_color="white")
        label6.configure(text_color="white")
        label7.configure(text_color="white")
        bgcolor("black")
        dark_mode_button.configure(text="Light Mode")

def dark_mode():
    global t
    if get_appearance_mode() == "Dark":
        t = "white"
        bgcolor("black")
    else:
        t = "black"

def scaleCreation(From: int, To: int, X: int, Y: int, default: str='0'):
        scale = CTkSlider(root, from_=From, to=To, progress_color="blue")
        scale.set(default)
        scale.place(relx=X, rely=Y, anchor = "center")
        return scale
def labelCreation(text: str, X: float, Y: float, font: tuple=("Arial", 20)):
    dark_mode()
    label = CTkLabel(root, text=text, font=font, text_color=t, compound="center", wraplength=300)

    label.place(relx=X, rely=Y, anchor="center")
    return label




#Enter Shape
label1 = labelCreation("Enter Shape:",  0.5, 0.02)

#Enter # of shapes
label2 = labelCreation("Enter # of shapes:", .5, .12)
numShapes = scaleCreation(1, 200, 0.5, .18, 100)

label3 = labelCreation("Enter Pen Size:", .5, .25)
penSize = scaleCreation(1, 100, 0.5, .3, 30)

label4 = labelCreation("Enter Bounds:", .5, .35)
boundsSlider = scaleCreation(0, 300, 0.5, .4, 150)

label5 = labelCreation("Enter # of random colors:", .5, .45)
numColors = scaleCreation(1, 200, 0.5, .5, 100)

label6 = labelCreation("Enter Speed: (0=Max Speed)", .5, .55)
speedSlider = scaleCreation(0, 10, 0.5, .6, 0)
label7 = labelCreation("",0.5,0.7)

#Draw and Clear Buttons
button = CTkButton(root, text="DRAW", corner_radius=32, fg_color="black", hover_color="dark blue", border_color="sky blue", border_width=2)
button2 = CTkButton(root, text="CLEAR/RESET", corner_radius=32, fg_color="black", hover_color="dark blue", border_color="sky blue", border_width=2)
# img = Image.open("lightmode.png")
# click_button = Image(CTkImage(img))
dark_mode_button = CTkButton(root, text="Dark Mode", corner_radius=32, fg_color="black", hover_color="dark blue", border_color="sky blue", border_width=2, command=dark_mode_button_func)



dark_mode_button.place(relx=0.5, rely=0.8, anchor = "center")
button.place(relx=0.5, rely=0.85, anchor = "center")
button2.place(relx=0.5, rely=0.9, anchor = "center")


colors = []

def generateColors(num: int):
    global colors
    colors = []
    for i in range(num): 
        colors.append('#%06X' % randint(0, 0xFFFFFF))

def buildFlower():
    pendown()
    for i in range(10):
        forward(100)
        left(100)

def buildSquare():
    pendown()
    for i in range(4):
        forward(100)
        left(90)

def buildCircle(size: float):
    pendown()
    circle(size)

def buildTriangle():
    for i in range(3):
        forward(100)
        left(120)

def buildStar():
    for i in range(5):
        forward(100)
        left(144)

def buildHexagon():
    for i in range(6):
        forward(100)
        left(60)

def buildOctagon():
    for i in range(8):
        forward(100)
        left(45)

def buildPentagon():
    for i in range(5):
        forward(100)
        left(72)

def buildHeptagon():
    for i in range(7):
        forward(100)
        left(51.43)

def buildNonagon():
    for i in range(9):
        forward(100)
        left(40)

def buildDecagon():
    for i in range(10):
        forward(100)
        left(36)
    
def buildSwirl():
    for steps in range(100):
        forward(steps)
        right(30)


def repeatShape(x: callable):
    setheading(0)
    global bounds
    int(bounds)
    num = int(numShapes.get())
    
    for i in range(num):
        pensize(int(penSize.get())) #This allows for scaling of pen while drawing
        bounds = int(boundsSlider.get())
        if len(colors) == 1:
            pencolor(colors[0]) #If only one color is generated, use that color
        pencolor(colors[randint(0,len(colors)-1)]) #Randomly select a color from the list
        pendown()
        speed(int(speedSlider.get()))
        text = f"Now creating {int(numShapes.get())} shapes of {dropdown.get()} with a pen size of {int(penSize.get())} and bounds of {int(boundsSlider.get())} with {int(numColors.get())} random colors at a speed of {int(speedSlider.get()) if int(speedSlider.get()) != 0 else '1000'}"
        label7.configure(text=text)
        #Run shape function
        x()
        #Move to new location
        penup()
        randomW = randint(-window_width()//2+bounds, window_width()//2-bounds) 
        randomH = randint(-window_height()//2+bounds, window_height()//2-bounds)
        goto(randomW, randomH)

window_open = True
def close_window():
    global window_open
    window_open = False
    root.destroy()

'''command() is the function that will be called when the draw button is clicked.
   It will call the repeatShape function with the appropriate shape function 
   based on the dropdown menu selection.'''

def command():
    try:
        hideturtle()
        global bounds
        bounds = int(boundsSlider.get())
        selection = dropdown.get()
        #Generate colors
        global colors
        generateColors(int(numColors.get()))
        # speed(speedSlider.get())
        if selection == options[0]:
            repeatShape(buildFlower)
        elif selection == options[1]:
            repeatShape(buildSquare)
        elif selection == options[2]:
            repeatShape(lambda: buildCircle(100))
        elif selection == options[3]:
            repeatShape(buildTriangle)
        elif selection == options[4]:
            repeatShape(buildStar)
        elif selection == options[5]:
            repeatShape(buildPentagon)
        elif selection == options[6]:
            repeatShape(buildHexagon)
        elif selection == options[7]:
            repeatShape(buildOctagon)
        elif selection == options[8]:
            repeatShape(buildSwirl)
        elif selection == options[9]:
            repeatShape(buildHeptagon)
        elif selection == options[10]:
            repeatShape(buildNonagon)
        elif selection == options[11]:
            repeatShape(buildDecagon)
        else:
            label7.configure(text="please input a valid shape")
            done()
        showturtle()
    except (Terminator, TclError): #Raised when the user exits before drawing has finished
        pass

'''superClear() is the function that will be called when the clear button is clicked.
   It will clear the screen, reset the number of shapes, pensize, numColors, and bounds to their
   default values, and update the canvas.'''
def superClear():
    setheading(0)
    clear()
    numShapes.set(100)
    penSize.set(30)
    boundsSlider.set(150)
    numColors.set(100)
    label7.configure(text="")
    done() #This is necessary for turtle to stop drawing if clicked before drawing is finished
    
def on_close():
    root.destroy()


root.protocol("WM_DELETE_WINDOW",  on_close)

button.configure(command=command)
button2.configure(command=superClear)
    
root.protocol("WM_DELETE_WINDOW", close_window)
root.mainloop()
print("Thank you for using my program!")
