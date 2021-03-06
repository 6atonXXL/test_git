from django.db import models

# Create your models here.
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 200)
    phone = models.CharField(max_length = 200)
    
    def __str__(self):
        return str(f'id: {self.id}')
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        