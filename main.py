import turtle
import math
#Арсений делает квадрат
def square (x, y, size, color, angle)
turtle.goto(x,y)
turtle.left(angle)
turtle.pendown()
turtle.pencolor(color)
turtle.left(angle)
turtle.forward(size)
turtle.left(90)
turtle.forward(size)
turtle.left(90)
turtle.forward(size)
turtle.left(90)
turtle.forward(size)
turtle.left(90)
fillcolor(color)
turtle.penup()
pass



turtle.penup()
turtle.goto(35, 35)
turtle.right(90) # Повернуть курсор на 90 градусов вправо
turtle.pendown()
turtle.forward(70) # Пройти вперед расстояние 70, если курсор опущен, то будет нарисована линия по пути слоедования

turtle.right(90)
turtle.forward(70)

turtle.right(90)
turtle.forward(70)

turtle.right(90)
turtle.forward(70)

turtle.penup()
turtle.goto(45, 35)
turtle.right(225)
turtle.pendown()
turtle.forward(70)

turtle.left(90)
turtle.forward(70)

turtle.left(135) # Повернуть курсор влево на 135 градусов
turtle.forward(100)

turtle.done()


turtle.color("blue") # Устанавливаем цвет черепашки
turtle.penup() # Поднимаем курсор
turtle.goto(-110, -25) # Переходим по нужным координатам
turtle.pendown() # Опускаем курсор
turtle.circle(45) # Рисуем круг с радиусом 45

turtle.color("black")
turtle.penup()
turtle.goto(0, -25)
turtle.pendown()
turtle.circle(45)

turtle.color("red")
turtle.penup()
turtle.goto(110, -25)
turtle.pendown()
turtle.circle(45)

turtle.color("yellow")
turtle.penup()
turtle.goto(-55, -75)
turtle.pendown()
turtle.circle(45)

turtle.color("green")
turtle.penup()
turtle.goto(55, -75)
turtle.pendown()
turtle.circle(45)

turtle.color("black")
turtle.penup()
turtle.goto(0, 80)
turtle.pendown()
turtle.write("Olympic Symbol") # Вместо еще одного круга выводим надпись "Olympic Symbol"

turtle.done()







