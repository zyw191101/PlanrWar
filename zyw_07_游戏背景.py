# 背景交替滚动的思路确定
"""
解决办法：
１．创建两张背景图像精灵
   -第１张完全和屏幕重合
   -第２章在屏幕的正上方
２．两张图像一起向下运动
　　-self.rect.y += self.speed
3.当任意背景精灵的　rect.y >= 屏幕的高度说明已经移动到屏幕的下方
4.当移动到屏幕下方的这张图像设置到屏幕的正上方
　　- rect.y = -rect.height
"""

# 设计游戏背景类
"""
GameSprites 的update 方法不能满足背景的需求，所以新建一个背景类继承自GameSprites


Background
__init__(self,is_alt)
update(self)

初始化方法：
直接指定背景图片
is_alt判断是否是另一张图像
    Flase　表示第一章图像
    True表示另一张图像，在屏幕正上方

update()方法
    判断是否移动出屏幕，如果是，将图像设置到屏幕的正上方，从而实现交替波动
"""

# 背景精灵的基本实现
"""1.背景精灵的基本实现
在plane_sprites新建一个Background继承自GameSprites
class Background(GameSprite):
    # Background是一个单词,游戏背景精灵
    def update(self):
        # 调用父类方法
        super().update()
        # 判断是否移动出屏幕，如果是，将图像设置到屏幕的正上方，从而实现交替波动
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height

"""

# 在plane_main.py中显示背景精灵
"""
1.在__create_sprites方法中创建精灵和精灵组
２．在__update_sprites方法中，让精灵组调用 update() 和 draw()方法
    __create_sprites方法

"""

# 利用初始化方法，简化背景精灵创建
"""
在主程序中，创建的两个背景精灵，传入了相同的图像路径
创建第二个背景精灵时，在主程序中，设置背景精灵的图像位置

思考：精灵的初始位置的设置，应该由主程序负责？还是由精灵自己负责
答案：由精灵自己负责

根据面向对象设计规则，应该将对象的职责，封装到类的内部
尽量简化程序调用一方的代码调用


在Background类中指定一个初始化方法：
１．直接指定背景图片
２．is_alt判断是否是另一张图像
    Flase　表示第一张图像
    True表示另一张图像，在屏幕正上方    

"""