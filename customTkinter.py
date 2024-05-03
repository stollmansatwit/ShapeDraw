from customtkinter import *
from turtle import * 
from customtkinter import *
from random import randint
from PIL import Image, ImageTk
import pygetwindow
import pyautogui
import threading



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
running = True

#Close the main window...
def close_app():
    global running
    running = False
    clear()
    label7.configure(text="Now Closing...", font=("Arial", 30))
    root.title("Bye Bye!")
    screen.cv._rootwindow.title("Bye Bye!")
    smiley = "😊"
    write(smiley, font=("Arial", 100))
    root.quit()


#Dropdown menu
options = ["Flower", "Square", "Circle", "Triangle", "Star", "Pentagon", 
           "Hexagon", "Octagon", "Swirl", "Heptagon", "Nonagon", "Decagon", "Dot", "Six Sided Star"]

# Create a CTkComboBox
dropdown = CTkComboBox(master=root, values=options, fg_color="sky blue")
dropdown.place(relx=0.5, rely=0.07, anchor="center")

def screenshot(name: str = 'result'):
    if entry.get() != "":
        name = entry.get()
    path = 'images\\' + name + '.png'
    # titles = pygetwindow.getAllTitles()
    window = pygetwindow.getWindowsWithTitle('Python Turtle Graphics')[0]
    left, top = window.topleft
    right, bottom = window.bottomright
    pyautogui.screenshot(path)
    im = Image.open(path)
    im = im.crop((left+20, top+40, right-20, bottom-20))
    im.save(path)
    im.show(path)
    entry.delete(0, END)

#Dark Mode Button
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
        dark_mode_button.configure(text="Dark Mode")
        dropdown.configure(fg_color="sky blue")
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
        dropdown.configure(fg_color="dark blue")

#Making sure labels are created correctly depending on the appearance mode
def dark_mode():
    global t
    if get_appearance_mode() == "Dark":
        t = "white"
        bgcolor("black")
    else:
        t = "black"

#Functions for creating scales and labels
def scaleCreation(From: int, To: int, X: int, Y: int, default: str='0'):
        scale = CTkSlider(root, from_=From, to=To, progress_color="blue")
        scale.set(default)
        scale.place(relx=X, rely=Y, anchor = "center")
        return scale
def labelCreation(text: str, X: float, Y: float, font: tuple=("Arial", 20)):
    dark_mode()
    label = CTkLabel(root, text=text, font=font, text_color=t, compound="center", wraplength=300, bg_color="transparent")
    label.place(relx=X, rely=Y, anchor="center")
    return label





label1 = labelCreation("Enter Shape:",  0.5, 0.02)

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
label7 = labelCreation("",0.5,0.67, ("Arial", 15))


entry = CTkEntry(root, width=150, corner_radius=32, border_color="sky blue", border_width=2, placeholder_text="Screenshot Name")
entry.place(relx=0.5, rely=0.75, anchor = "center")

#Draw and Clear Buttons
button = CTkButton(root, text="DRAW", corner_radius=32, fg_color="black",
                    hover_color="dark blue", border_color="sky blue",
                      border_width=2)

button2 = CTkButton(root, text="CLEAR/RESET", corner_radius=32, fg_color="black",
                     hover_color="dark blue", border_color="sky blue",
                       border_width=2)
# img = Image.open("lightmode.png")
# click_button = Image(CTkImage(img))
dark_mode_button = CTkButton(root, text="Dark Mode", corner_radius=32, fg_color="black",
                              hover_color="dark blue", border_color="sky blue", border_width=2,
                                command=dark_mode_button_func)

screenshot_button = CTkButton(root, text="Screenshot", corner_radius=32, fg_color="black",
                               hover_color="dark blue", border_color="sky blue", border_width=2,
                                 command=screenshot)


dark_mode_button.place(relx=0.5, rely=0.8, anchor = "center")
button.place(relx=0.5, rely=0.85, anchor = "center")
button2.place(relx=0.5, rely=0.9, anchor = "center")
screenshot_button.place(relx=0.5, rely=0.95, anchor = "center")


colors = []

def generateColors(num: int):
    global colors
    '''colors can be set to a certain color pallette or generated randomly.'''
    #colors = ['#A19542', '#4AA142', '#429EA1', '#4642A1','#9E42A1']
    # colors = ['#DE73E5', '#E57773', '#E5CB73','#A8E573','#73E5B0']
    #colors = ['#FF0000', '#FF7F00', '#FFFF00', '#00FF00', '#0000FF', '#4B0082', '#8B00FF']
    #colors = ['orange', 'Green', 'sky blue', 'Royal Blue', '#645CE0' ]
    colors = []
    for i in range(num): 
        colors.append('#%06X' % randint(0, 0xFFFFFF))

def buildShape(Range: int, f: int=100, l: int=100, r: int=0):
    global running
    for i in range(Range):
        if not running:
            break
        forward(f)
        left(l)
        right(r)

def buildFlower():
    buildShape(10, 100, 100)

def buildSquare():
    buildShape(4, 100, 90)

def buildCircle(size: float):
    circle(size)

def buildTriangle():
    buildShape(3, 100, 120)

def buildStar():
    buildShape(5, 100, 144)

def buildHexagon():
    buildShape(6, 100, 60)

def buildOctagon():
    buildShape(8, 100, 45)

def buildPentagon():
    buildShape(5, 100, 72)

def buildHeptagon():
    buildShape(7, 100, 51.43)

def buildNonagon():
    buildShape(9, 100, 40)

def buildDecagon():
    buildShape(10, 100, 36)

def buildSixSidedStar():
    setheading(0)
    for i in range(6):
        
        left(60)
        forward(100)
        right(120)
        forward(100)
    
def buildSwirl():
    for steps in range(100):
        forward(steps)
        right(30)



def repeatShape(x: callable):
    setheading(0)
    global bounds
    int(bounds)
    num = int(numShapes.get())
    global running
    
    for i in range(num):
        while(running):
            num = int(numShapes.get())
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

'''command() is the function that will be called when the draw button is clicked.
   It will call the repeatShape function with the appropriate shape function 
   based on the dropdown menu selection.'''

def command():
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
    elif selection == options[12]:
        repeatShape(lambda: buildCircle(1))
    elif selection == options[13]:
        repeatShape(buildSixSidedStar)
    else:
        label7.configure(text="please input a valid shape")
        done()

'''superClear() is the function that will be called when the clear button is clicked.
   It will clear the screen, reset the number of shapes, pensize, numColors, and bounds to their
   default values, and update the canvas.'''
def superClear():
    try:
        setheading(0)
        clear()
        numShapes.set(100)
        penSize.set(30)
        boundsSlider.set(150)
        numColors.set(100)
        label7.configure(text="")
        done() #This is necessary for turtle to stop drawing if clicked before drawing is finished
    except:
        pass

button.configure(command=command)
button2.configure(command=superClear)
#...Close windows
screen.cv._rootwindow.protocol("WM_DELETE_WINDOW", close_app)
root.protocol("WM_DELETE_WINDOW", close_app)


root.mainloop()
print("Thank you for using my program!")
