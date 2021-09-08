import pygame
from plane_sprites import *     # 这里注意，最好不要使用*，容易出错


class PlaneGame(object):
    """飞机大战主游戏类"""
    def __init__(self):
        print("游戏初始化")
        # １．创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # ２．创建游戏的时钟
        self.clock = pygame.time.Clock()
        # ３．调用私有方法，精灵和精灵组
        self.__create_sprites()
        # ４．设置定时器事件　-创建敌机１s
        pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)
    def __create_sprites(self):
        # 新建背景精灵和精灵组
        bg1 = Background()
        # 指定第二个背景图像的初始位置
        bg2 = Background(True)

        # 创建敌机精灵组
        self.back_group = pygame.sprite.Group(bg1,bg2)

        self.enemy_group = pygame.sprite.Group()

        # 创建英雄的精灵和精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)


    def start_game(self):
        print("开始游戏...")
        while True:
            # 1.设置刷新频率
            self.clock.tick(FRAME_PER_SEC)
            # 2.事件监听
            self.__evevt_handler()
            # 3.碰撞检测
            self.__check_collide()
            # 4.更新/绘制精灵组
            self.__update_sprites()
            # 5.更新显示器
            pygame.display.update()


    def __evevt_handler(self):
        for event in pygame.event.get():
            # 判断事件类型是否是退出事件（用户是否点击了关闭按钮）
            if event.type == pygame.QUIT:
                # 调用游戏关闭　　静态方法
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                #　创建敌机精灵
                enemy = Enemy() # 敌机精灵的图片已经被封装到类的出事化方法中，所以（）不需要添加任何参数
                # 将精灵添加到精灵组
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
        # 使用键盘提供的方法获取键盘按键，　--按键元组
        keys_pressed = pygame.key.get_pressed()
        # 判断是否按下了方向键
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0



    def __check_collide(self):

        # 子弹摧毁飞机
        pygame.sprite.groupcollide(self.enemy_group, self.hero.bullets, True,True)

        # 敌机撞毁英雄，
        enemies_list = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
        # 判断列表是否有内容
        if len(enemies_list) > 0:
            # 让英雄牺牲
            self.hero.kill()
            # 结束游戏
            self.__game_over()

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束")

        pygame.quit()
        exit()

# 让当前的主程序也可以当做模块被导入(判断__name__的属性)
if __name__ == '__main__':

    # 创建游戏对象
    game = PlaneGame()
    # 运行游戏
    game.start_game()