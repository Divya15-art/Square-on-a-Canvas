import turtle

# creating canvas 
turtle.Screen().bgcolor("orange")

sc = turtle.Screen()
sc.setup(400, 300)

turtle.title("Welcome to Turtle Window")

# turtle object creation
window = turtle.Turtle()
for i in range(4) :
    window.right(90)
    window.forward(100)
    window.fillcolor("Black")
    
turtle.mainloop()