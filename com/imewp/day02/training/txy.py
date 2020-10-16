# 使用turtle库函数绘制一个包含9个同心圆的靶盘

import turtle

turtle.setup(1000, 500)
turtle.pensize(2)
turtle.penup()
turtle.seth(180)
for i in range(10):
    turtle.circle(30 + (i - 1) * 20)
    turtle.penup()
    turtle.seth(-90)
    turtle.fd(20)
    turtle.seth(0)
    turtle.pendown()
turtle.done


