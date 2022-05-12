
from django.db import models

# Create your models here.


class Records(models.Model):
    rdate = models.DateTimeField()
    rbuilding = models.CharField(max_length=20)
    rfloor = models.CharField(max_length=20)
    rcat = models.CharField(max_length=20)
    rphoto = models.ImageField(null = True, blank=True)
    isDelete = models.BooleanField(default = False)
    isHandle = models.BooleanField(default=False)
    # def __str__(self):
    #     return "&s-%d-%d"%(self.rdate,self.rbuilding,self.rfloorm,self.rcat,self.rphoto)

    # class Meta:
    #     # 定义该 model 在数据中的表名称:
    #     # db_table = 'visitors'
    #
    #     db_table = 'project'
    def to_dict(self):
        return {
            'rdate': self.rdate,
            'rbuilding': self.rbuilding,
            'rfloor': self.rfloor,
            'rcat': self.rcat,
            'rphoto': self.rphoto,
            'isDelete': self.isDelete,
            'isHandle': self.isHandle,
        }