import turtle

turtle.showturtle()
turtle.write("hello world")
turtle.forward(100)
turtle.color('red')
turtle.forward(100)
turtle.left(90)
turtle.color('green')
turtle.forward(100)
turtle.goto(0,0)

turtle.penup()
turtle.goto(0,100)
turtle.pendown()
turtle.circle(50)

turtle.done()   # 保持窗口存在
