
from django.db import models

# Create your models here.


class Records(models.Model):
    rdate = models.DateField()
    rbuilding = models.CharField(max_length=20)
    rfloor = models.CharField(max_length=20)
    rcat = models.CharField(max_length=20)
    rphoto = models.ImageField(null=True, blank=True)
    isDelete = models.BooleanField(default=False)
    isHandle = models.BooleanField(default=False)
    # def __str__(self):
    #     return "&s-%d-%d"%(self.rdate,self.rbuilding,self.rfloor,self.rcat,self.rphoto)
    def to_dict(self):
        return {
            'rdate': self.rdate,
            'rbuilding': self.rbuilding,
            'rfloor': self.rfloor,
            'rcat': self.rcat,
            'rphoto': self.rphoto,
            'isDelete': self.isDelete,
            'isHandle': self.isHandle
        }

class Users(models.Model):
    username = models.CharField(max_length=20)
    passwd = models.CharField(max_length=32)
    def to_dict(self):
        return{
            'username': self.username,
            'passwd': self.passwd
        }