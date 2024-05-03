from turtle import *
from tkinter import *
from tkinter import ttk
# from customtkinter import *
from random import randint

setup(width=1920, height=1080)
screen = Screen()
canvas = screen.cv
screen.cv._rootwindow.resizable(False, False)
shape("turtle")

#Mini Window
root = Tk()
root.title("Draw Shapes")
root.geometry("400x600")
root.configure(bg="pink")

def scaleCreation(From: int, To: int, X: int, Y: int, Length: int=100, Bg: str="white", default: int=0):
    scale = Scale(root, from_=From, to=To, orient=HORIZONTAL, length=Length, bg=Bg)
    scale.set(default)
    scale.pack()
    scale.place(x=X, y=Y)
    return scale

def labelCreation(text: str, X: int, Y: int, font: tuple=("Arial", 12), bg: str="pink", fg: str="black"):
    label = Label(root, text=text, font=font, bg=bg, fg=fg)
    label.pack()
    label.place(x=X, y=Y)
    return label

#Dropdown menu
style = ttk.Style()
style.configure("TMenubutton.menu", font=("Arial", 100))
options = ["Flower", "Square", "Circle", "Triangle", "Star", "Pentagon", "Hexagon", "Octagon", "Swirl", "Heptagon", "Nonagon", "Decagon"]
value_inside = StringVar(root)

dropdown = ttk.OptionMenu(root, value_inside, options[0], *options) #options[0] allows for consistency when unpacking
dropdown.pack()
dropdown.place(x=222, y=0)

#Enter Shape
label1 = labelCreation("Enter Shape:", 100, 0)

#Enter # of shapes
label2 = labelCreation("Enter # of shapes:", 100, 50)
numShapes = scaleCreation(1, 200, 150, 75, 100, "white", 100)

#Enter Pen Size
label3 = labelCreation("Enter Pen Size:", 100, 125)
penSize = scaleCreation(1, 100, 150, 150, 100, "white", 30)

#Enter Bounds
label4 = labelCreation("Enter Bounds:", 100, 200)
boundsSlider = scaleCreation(0, 300, 150, 225, 100, "white", 150)

#Enter Number of Colors
label5 = labelCreation("Enter # of random colors:", 100, 275)
numColors = scaleCreation(1, 200, 150, 300, 100, "white", 100)

#Enter Speed
label6 = labelCreation("Enter Speed: (0=Max Speed)", 100, 350)
speedSlider = scaleCreation(0, 10, 150, 375, 100, "white", 100)

#Draw and Clear Buttons
button = Button(root, text="DRAW", bg="red", fg="white", pady=10, padx=10)
button.pack()
button.place(x=100, y=450)
button2 = Button(root, text="CLEAR/RESET", bg="red", fg="white", pady=10, padx=10)
button2.pack()
button2.place(x=200, y=450)

# speed(700)
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
    num = int(numShapes.get())
    for i in range(num):
        pensize(penSize.get()) #This allows for scaling of pen while drawing
        bounds = boundsSlider.get()
        if len(colors) == 1:
            pencolor(colors[0]) #If only one color is generated, use that color
        pencolor(colors[randint(0,len(colors)-1)]) #Randomly select a color from the list
        pendown()
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
    try:
    
        hideturtle()
        global bounds
        bounds = boundsSlider.get()
        canvas.update()
        selection = value_inside.get()
        numColors.get()
        #Generate colors
        global colors
        generateColors(numColors.get())
        speed(speedSlider.get())
        
        
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
            print("please input a valid shape")
        showturtle()
    except Terminator: #Raised when the user exits before drawing has finished
        pass
    except TclError: #Same as Terminator but only for circles because repeatshape is running the circle function
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
    canvas.update()
    done() #This is necessary for turtle to stop drawing if clicked before drawing is finished
    
    
button.config(command=command)
button2.config(command=lambda: superClear())
    
done()
root.mainloop()
print("Thank you for using my program!")

