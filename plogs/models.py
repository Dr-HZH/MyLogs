from django.db import models

# Create your models here.
from django.utils.datetime_safe import datetime

from django.db import models

# 创建一个数据库user表模型
from MyLogs.settings import MEDIA_URL


class Avatar(models.Model):
    # 如果没有的话，默认会生成一个名称为 id 的列，如果要显示的自定义一个自增列
    AvatarId = models.AutoField(primary_key=True)
    # 类里面的字段代表数据表中的字段(username)，数据类型则由CharField（相当于varchar）
    AvatarName = models.CharField(max_length=100)
    AvatarSchool = models.CharField(max_length=100, default="WHU")
    AvatarMajor = models.CharField(max_length=100, default="信息管理与信息系统")
    AvatarProfile = models.TextField(null=True)
    AvatarAddress = models.TextField(null=True)
    AvatarPhone = models.CharField(max_length=100, null=True)
    AvatarMail = models.TextField(null=True)
    AvatarComment = models.TextField(null=True)
    AvatarPhoto = models.ImageField(upload_to="static", null=True)


class plog(models.Model):
    plog_id = models.IntegerField(primary_key=True, auto_created=True, verbose_name="id")
    plog_title = models.CharField(max_length=100)
    plog_content = models.TextField()
    plog_datetime = models.DateTimeField(default=datetime.now)
    plog_abstract = models.TextField(null=True)
    plog_img1 = models.ImageField(upload_to='media', null=True)
    plog_img2 = models.ImageField(upload_to='media', null=True)
    plog_img3 = models.ImageField(upload_to='media', null=True)
    plog_img4 = models.ImageField(upload_to='media', null=True)
    plog_img5 = models.ImageField(upload_to='media', null=True)
    plog_img6 = models.ImageField(upload_to='media', null=True)
    plog_img7 = models.ImageField(upload_to='media', null=True)
    plog_img8 = models.ImageField(upload_to='media', null=True)
    plog_img9 = models.ImageField(upload_to='media', null=True)
