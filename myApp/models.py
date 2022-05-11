
from django.db import models

# Create your models here.


class Records(models.Model):
    rdate = models.DateTimeField()
    rplace = models.CharField(max_length=20)
    rnum = models.CharField(max_length=20)
    rcat = models.CharField(max_length=20)
    rphoto = models.ImageField(null = True, blank=True)
    isDelete = models.BooleanField(default = False)
    def __str__(self):
        return "&s-%d-%d"%(self.rdate,self.rplace,self.rnum,self.rcat,self.rphoto)