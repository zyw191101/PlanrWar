# 目标
"""
１．设计英雄和子弹类
２．使用pygame.key.get_pressed()移动英雄
３．发射子弹
"""

# 设计英雄
"""英雄需求
１．游戏启动后，英雄出现在屏幕的水平中间位置，距离距离屏幕底部120像素（初始化方法）
２．英雄每隔0.5秒发射一次子弹，每次三连发(定时器)
英雄默认不会移动，需要通过　左/右方向键，控制英雄在水平方向移动

１．初始化方法：
    指定英雄图片
    初始速度 = 0　--英雄默认静止不动
    定义bullet子弹精灵组　保存子弹精灵
２．重写update()方法
    英雄需要水平移动
    并且需要保证不能移出屏幕
增加bullet属性，记录所有子弹精灵
增加fire方法　用于发射子弹

"""

# 创建英雄
"""
1.准备英雄类
　１．在plane_sprites新建Hero类
　２．重写初始化方法，直接指定图片名称
　３．设置英雄的初始位置


pygame.Rect类(方便我们设置精灵的位置)包括
    x,y,
    left,right,top,bottom
    center,certerx,centery
    size,width,height



"""

# 绘制英雄
"""
1.在　__create_sprites,添加　英雄精灵和英雄精灵组
    后续要针对英雄做碰撞检测　以及发射子弹
 
    所以英雄需要单独定义成属性 (这样我们才能够在其他方法中直接使用英雄这个对象)
２．在__update_sprites，让英雄级精灵组　调用　update和draw 方法


"""

# 移动英雄位置
"""
１．在Hero类中重写update方法
    用速度speed和英雄rect.x进行叠加
    不需要调用父类方法　--父类方法只是实现了单纯的垂直运动
２．在__event_handler方法中根据左右方向键设置英雄的速度
    向右　２
    向左　２
    其他　０　


"""

# 控制英雄的边界
"""
在Hero类的　update()方法判断英雄是否超出屏幕边界
    right = x + width　利用right属性可以非常容易的针对右侧设置精灵位置


"""



# 设计子弹
"""子弹需求
１．子弹从英雄的正上法发射沿直线向　上方飞行
２．飞出屏幕后，需要从精灵组中删除

"""

# 1.添加发射子弹事件
"""
1.1pygame的定时器　使用套路十分固定
[定义常量]=>[在初始化方法中设置事件]=>[在游戏循环中监听事件]
    １．定义定时器常量　--eventid
    ２．在初始化方法中，调用set_timer方法设置定时器事件
    ３．在游戏循环中，监听定时器事件
"""

# 2.定义子弹类
"""
需求：
子弹从英雄正上方发射沿直线向上方飞行
飞出屏幕后，需要从精灵组中删除
1.新建类
2.初始化方法指定名称，设置初始速度
３．重写update方法

"""

# 3.发射子弹
"""
1.在Hero的初始化方法中创建子弹精灵组属性
２．修改plane_main.py的__update_sprites方法，让子弹精灵组调用update和draw方法
３．实现fire()方法
    创建子弹精灵
    设置初始位置　－－在英雄的正上方
    将子弹添加到精灵组
    


"""

# 4.子弹三连发
"""

"""








# 按键捕获方式
"""
在pygame 中针对键盘按键的捕获，有两种方式
第一种方式判断　event.type == pygame.KEYDOWN
第二种方式
    １．首先使用pygame.key.get_pressed()返回所有按键元组
    ２．通过键盘常量，判断元组中　某一个按键是否被按下　--如果被按下，对应数值为　1
代码实现：
方式１：用户按下按键事件被处罚，但是只能触发一次，触发完成后，再想触发，需要再按一次
elif evnnt.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
    print("向右移动")
方式２：
# 返回所有按键的元组，如果某一个键被按下，对应的值会是１
key_pressed = pygame.key.get_pressed()
# 判断是否按下了方向键
if keys_pressed[pygame.K_RIGHT]:
    print("向右移动")
方式１／2优劣
方式１：用户必须要抬起按键才算一次按键事件，操作灵活性会大打折扣（半自动/栓动）
方式２：用户可以按住方向键不放，就能够实现持续向某一个方向移动了，操作灵活性更好（全自动）

"""

