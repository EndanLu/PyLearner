#!/usr/bin/python3

import turtle
import random

def Snake():
    # 设置窗口
    window = turtle.Screen()
    window.title("贪吃蛇")
    window.bgcolor("white")
    window.setup(width=600, height=600)

    # 创建蛇头
    head = turtle.Turtle()
    head.shape("square")
    head.color("green")
    head.penup()
    head.goto(0, 0)

    # 创建食物
    food = turtle.Turtle()
    food.shape("circle")
    food.color("red")
    food.penup()
    food.goto(random.randint(-280, 280), random.randint(-280, 280))

    # 定义移动函数
    def move():
        head.forward(20)

    # 绑定键盘事件
    window.onkey(move, "Up")
    window.onkey(move, "Down")
    window.onkey(move, "Left")
    window.onkey(move, "Right")

    # 开始游戏
    window.listen()
    turtle.mainloop()
