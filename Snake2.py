#!/usr/bin/python3

# 导入 pygame 模块
import pygame
import random

# 初始化 pygame
pygame.init()

# 设置屏幕大小和标题
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("贪吃蛇")

# 设置颜色常量
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 设置蛇的初始位置和方向
snake_x = 400
snake_y = 300
snake_direction = "right"
snake_body = [(snake_x, snake_y)]

# 设置食物的初始位置
food_x = random.randint(0, 79) * 10
food_y = random.randint(0, 59) * 10

# 设置游戏状态和得分
game_over = False
score = 0

# 设置时钟对象和帧率
clock = pygame.time.Clock()
FPS = 10

# 游戏主循环
while not game_over:
    # 处理事件队列
    for event in pygame.event.get():
        # 如果点击了关闭按钮，退出游戏
        if event.type == pygame.QUIT:
            game_over = True

        # 如果按下了方向键，改变蛇的方向（不能反向）
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "down":
                snake_direction = "up"
            elif event.key == pygame.K_DOWN and snake_direction != "up":
                snake_direction = "down"
            elif event.key == pygame.K_LEFT and snake_direction != "right":
                snake_direction = "left"
            elif event.key == pygame.K_RIGHT and snake_direction != "left":
                snake_direction = "right"

    # 根据蛇的方向，更新蛇头的位置（每次移动10像素）
    if snake_direction == "up":
        snake_y -= 10
    elif snake_direction == "down":
        snake_y += 10
    elif snake_direction == "left":
        snake_x -= 10
    else:
        snake_x += 10

    # 检查蛇头是否超出屏幕边界，如果是，游戏结束（也可以让蛇穿越边界）
    if snake_x < 0 or snake_x > 790 or snake_y < 0 or snake_y > 590:
        game_over = True

    # 检查蛇头是否撞到自己的身体，如果是，游戏结束（也可以让蛇穿过身体）
    if (snake_x, snake_y) in snake_body:
        game_over = True

    # 把新的蛇头位置添加到蛇身列表中，并删除最后一个元素（模拟前进效果）
    # 如果吃到食物，则不删除最后一个元素（模拟增长效果），并重新生成食物位置，并增加得分和帧率
    # 注意：这里有一定概率生成在蛇身上的食物，可以优化
    snake_body.insert(0, (snake_x, snake_y))

    if (snake_x, snake_y) == (food_x, food_y):
        food_x = random.randint(0, 79) * 10
        food_y = random.randint(0, 59) * 10
        score += 1
        FPS += 1

    else:
        del (snake_body[-1])

    # 填充背景色为黑色

screen.fill(BLACK)

# 绘制食物为红色矩形

pygame.draw.rect(screen, RED, (food_x, food_y, 10, 10))

# 绘制蛇身为白色