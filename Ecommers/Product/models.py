from django.db import models
from mptt.models import MPTTModel,TreeForeignKey

class Catogory(MPTTModel):
      name = models.CharField(max_length=255,blank=True)
      parent = TreeForeignKey("self",on_delete=models.PROTECT,null=True,blank=True)
      
      class MPTTMeta:
        order_insertion_by=['name']
      
      def __str__(self) -> str:
            return self.name

class Brand(models.Model):
      name = models.CharField(max_length=255,blank=True)
      def __str__(self) -> str:
            return self.name

     
class Products(models.Model):
      name = models.CharField(max_length=255,blank=True)
      description=models.TimeField(max_length=500)
      price =models.IntegerField()
      Brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
      type_isdigita=models.BooleanField(default=False)
      catogory = TreeForeignKey('Catogory',on_delete=models.SET_NULL,null=True,blank=True)
      def __str__(self) -> str:
            return self.name

     