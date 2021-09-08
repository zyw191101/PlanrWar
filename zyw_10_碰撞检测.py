# 了解碰撞检测方法
"""
pygame.sprite提供了两个非常方便的方法可以实现碰撞检测：
１．pygame.sprite.groupcollide()
    1.两个精灵组中的所有的精灵的碰撞检测
        groupcollide(group1,group2,dokill1,dokill2,collided = None) ->Sprites_dict
    2.如果将dokill设置为True,则发生碰撞的精灵将自动移除
    3.collide参数是用于计算碰撞的回调函数
        如果没有指定，则每个精灵必须有一个rect属性


２．pygame.sprite.spritecollide()
    判断某个精灵　和指定精灵组中的精灵的碰撞
    spritecollide(sprite,group,dokill,collide = None)  ->Sprites_list
  1.如果将dokill设置为True,则指定精灵组中发生碰撞的精灵将被自动移除
  2.collide参数是用于计算碰撞的回调函数
    如果没有指定，则每个精灵必须有一个rect属性
  3.返回精灵组中跟精灵发生碰撞的精灵列表






"""