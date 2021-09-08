import pygame
from plane_sprites import GameSprite
pygame.init()

# 编写游戏的代码
print("游戏代码")

# 创建游戏窗口
screen = pygame.display.set_mode((400,700))

#　绘制背景图像
bg = pygame.image.load("./images/background.png") # 有返回结果，定义变量接收

# 绘制英雄图像
hero = pygame.image.load("./images/me1.png")

# 创建敌机的精灵
enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png",2)

# 创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy)
# 创建时钟对象
clock = pygame.time.Clock()

# 1.定义rect（rectangle（矩形））记录飞机的  初始位置
hero_rect = pygame.Rect(200,500,102,126)

# 游戏循环 ->意味着游戏的正式开始
while True:
    # 可以指定循环体内部的代码执行的频率
    clock.tick(60)   # 无限循环内部的代码每秒钟执行(?)次

    # 监听事件
    for event in pygame.event.get():
        # 判断事件类型是否是退出事件（用户是否点击了关闭按钮）
        if event.type == pygame.QUIT:
            print("退出游戏")

            # quit()方法对所有的pygame的模块做一个卸载
            pygame.quit()

            # 直接退出系统
            exit()

    # ２．修改飞机的位置
    hero_rect.y -= 1
    if hero_rect.y <= -126:
        hero_rect.y = 700
    # 3.调用blit方法绘制图像
    screen.blit(bg,(0,0))
    screen.blit(hero,hero_rect)

    # 让精灵组调用两个方法
    # update -让组中的所有精灵更新位置
    enemy_group.update()
    # draw　－在screen上绘制所有精灵
    enemy_group.draw(screen)

    # 调用update方法更新显示
    pygame.display.update()





# 一开始＝１，会有飞机会飞出一片黑色的图像，是因为只刷新了飞机对象，而没有刷新画布即背景图
# 慎用，运行之后窗口关不上，严重的话会死机.(while True死机病毒的开端哈哈哈)
# print("英雄的原点 %d %d"%(hero_rect.x,hero_rect.y))
# print("英雄的尺寸　%d %d "%(hero_rect.width,hero_rect.height))
# # 测试size属性
# print("%d %d"%hero_rect.size)
pygame.quit()