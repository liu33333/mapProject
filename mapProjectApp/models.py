from django.db import models

class employee(models.Model):
    name = models.CharField(max_length=128, verbose_name='书籍名称')
    sex=models.IntegerField()