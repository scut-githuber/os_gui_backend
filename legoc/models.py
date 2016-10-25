from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# 不用专门写主键，会自动生成的

class LGNode(models.Model):
    # 存储xml转换而成的节点，是相对不变的一部分数据，对应xml里每个tag，简单的tag的desp字段可以为空
    name = models.CharField(max_length=50)
    desp = models.CharField(max_length=200, default='')
    code_path = models.CharField(max_length=300, default='')

# joyxee:使用django的user模块实现登录注册
# class LGUser(models.Model):
#     name = models.CharField(max_length=100)
#     mail = models.CharField(max_length=100)
#     # 前端 hash 后的密码
#     pwd = models.CharField(max_length=200)


class Project(models.Model):
    name = models.CharField(max_length=100)
    root_node = models.ForeignKey(LGNode)
    user = models.ForeignKey(User)
    # 持久化存储project对应的树结构
    pickle_path = models.CharField(max_length=200)


class NodeRef(models.Model):
    # 一个二元运算符表示一组关系， L is R 's ref
    node_left = models.ForeignKey(LGNode, related_name='node_left')
    node_right = models.ForeignKey(LGNode, related_name='node_right')
    # ref有两种：
    # 0, L is R's child
    # 1， L is R's left brother
    # 为了节省存储空间，不增加parent 和 right brother这两种关系
    ref = models.IntegerField()
