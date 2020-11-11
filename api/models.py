from django.db import models

# Create your models here.
class Type(models.Model):
    type_name = models.CharField(max_length=15)

    # 显示设置
    def __str__(self):
        return self.type_name

    class Meta:
        ordering = ['pk']

class Jingdian(models.Model):
    i_d = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    label = models.ForeignKey(Type, on_delete=models.DO_NOTHING)
    address = models.TextField()
    open_time = models.TextField()

    def __str__(self):
        return "<景点: %s>" % self.i_d

    class Meta:
        ordering = ['pk']