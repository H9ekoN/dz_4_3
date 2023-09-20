from django.db import models

# Create your models here.
class Advertisments(models.Model):
    class Meta:
        db_table = 'Advertisments'
    
    title = models.CharField('Заголовок', max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Отметьте если торг уместен')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'<Advertisement: Advertisement(id=1, title=Заголовок N1, price=100.000)>'