import pygame, sys, time, random

color_red = pygame.Color(255, 0, 0)
color_white = pygame.Color(255, 255, 255)
color_green = pygame.Color(0, 255, 0)
pygame.init()
screen = pygame.display.set_mode((600, 400))
screen.fill(color_white)
pygame.display.set_caption("贪吃蛇小游戏")
arr = [([0] * 41) for i in range(61)]  # 创建一个二维数组
x = 10  # 蛇的初始x坐标
y = 10  # 蛇的初始y坐标
foodx = random.randint(1, 60)  # 食物随机生成的x坐标
foody = random.randint(1, 40)  # 食物随机生成的y坐标
arr[foodx][foody] = -1
snake_lon = 3  # 蛇的长度
way = 1  # 蛇的运动方向

while True:
    screen.fill(color_white)
    time.sleep(0.1)
    for event in pygame.event.get():  # 监听器
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_RIGHT) and (way != 2):  # 向右移动且避免反向移动
                way = 1
            if (event.key == pygame.K_LEFT) and (way != 1):  # 向左移动且避免反向移动
                way = 2
            if (event.key == pygame.K_UP) and (way != 4):  # 向上移动且避免反向移动
                way = 3
            if (event.key == pygame.K_DOWN) and (way != 3):  # 向下移动且避免反向移动
                way = 4
    if way == 1:
        x += 1
    if way == 2:
        x -= 1
    if way == 3:
        y -= 1
    if way == 4:
        y += 1
    if (x > 60) or (y > 40) or (x < 1) or (y < 1) or (arr[x][y] > 0):  # 判断死亡（撞墙或自食）
        sys.exit()
    arr[x][y] = snake_lon
    for a, b in enumerate(arr, 1):
        for c, d in enumerate(b, 1):
            # 在二维数组中，食物为-1，空地为0，蛇的位置为正数
            if (d > 0):
                # print(a,c) #输出蛇的当前坐标
                arr[a - 1][c - 1] = arr[a - 1][c - 1] - 1
                pygame.draw.rect(screen, color_green, ((a - 1) * 10, (c - 1) * 10, 10, 10))
            if (d < 0):
                pygame.draw.rect(screen, color_red, ((a - 1) * 10, (c - 1) * 10, 10, 10))
    if (x == foodx) and (y == foody):   #蛇吃到食物
        snake_lon += 1    #长度+1
        while (arr[foodx][foody] != 0):    #刷新食物
            foodx = random.randint(1, 60)
            foody = random.randint(1, 40)
        arr[foodx][foody] = -1
    pygame.display.update()
