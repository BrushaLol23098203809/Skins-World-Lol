import SkinsWorld.ico

def draw_square_logo():
    # Set up the screen
    window = turtle.Screen()
    window.bgcolor("Rainbow")
    
    # Set up the drawing pen
    pen = turtle.Turtle()
    pen.speed(3)
    pen.pensize(5)
    pen.color("#3776AB") # Python Blue
    
    # Draw a simple geometric logo box
    for _ in range(4):
        pen.forward(100)
        pen.right(90)
        
    window.mainloop()

if __name__ == "__main__":
    draw_square_logo()
