from customtkinter import *
from turtle import * 
from random import randint
from PIL import Image, ImageTk
from tkinter import PhotoImage
import pygetwindow
import pyautogui
import multiprocessing

# Function to generate colors
def generateColors(num: int):
    '''Generate random colors.'''
    colors = []
    if num < 1:
        num = 1
    for i in range(num): 
        colors.append('#%06X' % randint(0, 0xFFFFFF))
    return colors

# Function to draw shapes
def draw_shape(shape_func, pen_size, bounds, num_colors, speed, num_shapes, colors, label):
    for i in range(num_shapes.get()):
        if not running.value:
            break
        penup()
        pensize(pen_size.get())
        bounds = bounds.value
        pencolor(colors[i % len(colors)])
        speed(speed.get())
        shape_func()
        penup()
        randomW = randint(-window_width()//2+bounds, window_width()//2-bounds) 
        randomH = randint(-window_height()//2+bounds, window_height()//2-bounds)
        goto(randomW, randomH)

# Function to handle drawing based on dropdown selection
def draw_command(selection, pen_size, bounds, num_colors, speed, num_shapes, colors, label):
    try:
        if not running.value:
            return    
        Screen().listen()
        hideturtle()
        bounds = bounds.value
        # Generate colors
        colors.value = generateColors(num_colors.get())
        functions = [buildFlower, buildSquare, lambda: buildCircle(100), buildTriangle, buildStar, buildPentagon, buildHexagon, buildOctagon, buildSwirl, buildHeptagon, buildNonagon, buildDecagon, lambda: buildCircle(1), buildSixSidedStar, writeSmile, writeSad, writeHeart, writeStar, writeSun, writeMoon, writeSnowflake, buildPenguin, buildOtter]
        for i in range(len(options)):
            if selection == options[i]:
                draw_shape(functions[i], pen_size, bounds, num_colors, speed, num_shapes, colors, label)
                return
        if selection != "":
            draw_shape(lambda: write(selection, font=("Arial", pen_size.get()), align="center"), pen_size, bounds, num_colors, speed, num_shapes, colors, label)
            return
        label.configure(text="please input a valid shape or text")
        done()
        return
    except Exception as e:
        print("An error occurred", e)

# Function to clear the screen
def super_clear():
    global running
    if not running.value:
        return
    running.value = False
    try:
        setheading(0)
        clear()
        numShapes.set(100)
        penSize.set(30)
        boundsSlider.set(150)
        numColors.set(100)
        label7.value = ""
        done()  # This is necessary for turtle to stop drawing if clicked before drawing is finished
    except:
        pass

if __name__ == "__main__":
    # Shared variables between processes
    running = multiprocessing.Value('b', True)
    numShapes = multiprocessing.Value('i', 100)
    penSize = multiprocessing.Value('i', 30)
    boundsSlider = multiprocessing.Value('i', 150)
    numColors = multiprocessing.Value('i', 100)
    colors = multiprocessing.Array('i', [randint(0, 0xFFFFFF) for _ in range(numColors.get())])
    label7 = multiprocessing.Array('c', b'')

    # Mini Window
    root = CTk()

    # Dropdown menu
    options = ["Flower", "Square", "Circle", "Triangle", "Star", "Pentagon", 
               "Hexagon", "Octagon", "Swirl", "Heptagon", "Nonagon", "Decagon",
               "Dot", "Six Sided Star", "Smile", "Sad", "Heart", "Star icon",
               "Sun", "Moon", "Snowflake", "Penguin", "Otter"]

    # Rest of your GUI setup code...

    # Draw and Clear Buttons
    button = CTkButton(root, text="DRAW", corner_radius=32, fg_color="black",
                        hover_color="dark blue", border_color="sky blue",
                        border_width=2, bg_color="transparent")

    button2 = CTkButton(root, text="CLEAR/RESET", corner_radius=32, fg_color="red",
                        hover_color="dark blue", border_color="sky blue",
                        border_width=2)

    # Set commands for buttons
    button.configure(command=lambda: draw_command(dropdown.get(), penSize, boundsSlider, numColors, speedSlider, numShapes, colors, label7))
    button2.configure(command=super_clear)

    # Rest of your GUI setup code...

    # Run the main loop
    root.mainloop()

    # Final message
    print("\nThank you for using my program!")
