import random
import pygame

# 设置屏幕大小的常量
SCREEN_RECT = pygame.Rect(0,0,480,700)
# 刷新的帧率
FRAME_PER_SEC = 60      # (FPS　--frame per second --每秒刷新频率)
# 创建敌机的定时器事件（常量）
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 创建敌机子弹定时器事件（常量）
HERO_FIRE_EVENT = pygame.USEREVENT +1

class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""
    def __init__(self,image_name,speed=1):
        #　调用父类的初始化方法
        super().__init__()
        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed =speed
    def update(self):

        # 在屏幕的垂直方向上移动
        self.rect.y += self.speed


class Background(GameSprite):
    """Background是一个单词,游戏背景精灵"""

    def __init__(self,is_alt=False):
        # alter改变
        # 1.调用父类方法实现精灵的创建（image/rect/speed）
        super().__init__("./images/background.png")
        # 2.判断是否是交替图像，如果是，需要设置初始位置
        if is_alt:
            self.rect.y = -self.rect.height
    def update(self):
        # 调用父类方法
        super().update()
        # 判断是否移动出屏幕，如果是，将f图像设置到屏幕的正上方，从而实现交替波动
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机精灵"""
    def __init__(self):

        # 调用父类方法，创建敌机精灵
        super().__init__("./images/enemy1.png")
        # 指定敌机的初始速度 1-3
        self.speed = random.randint(1,3)
        # 指定敌机的初始随机位置
        self.rect.bottom = 0 # bottom 是pygame 自带的属性，这样飞机会有飞入屏幕的效果，而不是突兀出现
        # 使飞机能够从最右侧飞出（飞机紧贴屏幕边缘）
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0,max_x)

    def update(self):

        # 调用父类方法，保持垂直方向的飞行
        super().update()
        # 判断是否飞出屏幕，如果是，需要从精灵组删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            # 将敌机精灵销毁
            self.kill()
    def __del__(self):
        print("敌机销毁%s"%self.rect)


class Hero(GameSprite):
    """英雄精灵"""

    def __init__(self):
        # 1.调用父类方法，，设置image&speed
        super().__init__("./images/me1.png",0)

        # 2.设置英雄的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        # 建立子弹的精灵组
        self.bullets = pygame.sprite.Group()
    def fire(self):

        for i in (0,1,2):     # 三连发
            # 创建子弹精灵
            bullet = Bullet()
            # 设置精灵的位置
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx
            self.bullets.add(bullet)

    def update(self):
        # 英雄在水平方向位置
        self.rect.x += self.speed
        # 控制英雄不能离开屏幕
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right  > SCREEN_RECT.right:   # right = x + width因为屏幕x的初始值是０,所以屏幕right = 屏幕宽度width
            self.rect.right = SCREEN_RECT.right


class Bullet(GameSprite):
    def __init__(self):
        super().__init__("./images/bullet1.png",speed=-3)

    def update(self):

        super().update()

        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        print("del方法就是让子弹被销毁可视化")
