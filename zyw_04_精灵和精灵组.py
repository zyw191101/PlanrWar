# 1.精灵和精灵组
"""
在刚刚完成的案例中，图像加载，位置变化，绘制图像　都需要程序员编写代码分别处理
为了简化开发步骤，pygame提供两个类
    pygame.sprite.Sprite --存储　图像数据image和 位置rect  的对象
    pygame.sprite.Group

精灵：（需要派生子类）
属性：
image 记录图像数据
rect 记录在屏幕上的位置
方法：
update(*args):更新精灵位置
kill():从所有组中删除

精灵组：
__init__(self,*精灵)：
add(*sprites):想组中增加精灵
sprites():返回所有精灵列表
update(*args):让组中所有精灵调用update方法
draw(Surface):将组中所有精灵的image，绘制到Surface的rect位置

                游戏循环
游戏初始化        精灵组.update()
创建精灵        　精灵组.draw(screen)
创建精灵组        pygame.display.update()

"""

# 2.派生精灵子类
"""
１．新建一个plane_sprites.py文件
２．定义GroupSprite继承自pygame.sprite.Sprite
注意：
如果一个类的　父类不是　object
在重写初始化方法时，一定要先super()一下父类的__init__方法
保证父类中实现的__init__代码能够被正常执行


GameSprite
属性：
image   精灵图像使用image_name加载
rect    精灵大小，默认使用图像大小
speed   精灵移动速度，默认为１

方法：
__init__(self,image_name,speed = 1):
update(self)
update 每次更新屏幕时在游戏循环内使用
    让精灵的　self.rect.y += self.speed

提示：
    image的get_rect()方法
    可以返回pygame.Rect(0,0,图像宽，图像高)的对象

"""

# 3.使用游戏精灵和精灵组创建敌机
"""
使用刚刚派生的游戏精灵　和精灵组创建敌机并且实现敌机动画
步骤：
１．使用from导入plane_sprites模块
    from导入的模块可以直接使用
    import导入的模块需要通过模块名.来使用
２．在游戏初始化创建精灵对象和精灵组对象
３．在游戏循环中　让精灵组分别调用　update()和draw(screen)方法

职责：
１．精灵
    封装图像image，位置rect和速度speed
    提供update()方法，根据游戏需求，更新位置rect
２．精灵组
    包含多个精灵对象
    update方法，让精灵组中的所有精灵调用update方法更新位置
    draw(screen)方法，在screen上绘制精灵组中的所有精灵
"""