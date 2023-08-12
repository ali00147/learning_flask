import turtle
t= turtle.Turtle()
t.speed(50)
t.left(90)

def branch(length,t):
    if length<=50:
        t.forward(length)
        t.right(20)
        t.left(40)
        branch(length-15,t)
        t.right(20)
        t.backward(length)
    branch(100,t)
    turtle.mainloop()
