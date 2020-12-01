from django.db import models
from django.urls import reverse


# Create your models here.

class videojuegos(models.Model):
    name = models.CharField(max_length=200)
    LOAN_PG = (
        ('p3', 'PEGI 3'),
        ('P7', 'PEGI 7'),
        ('P12', 'PEGI 12'),
        ('P16', 'PEGI 16'),
        ('P18', 'PEGI 18'),
    )

    pegi = models.CharField(
        max_length=3,
        choices=LOAN_PG,
        blank = True,
        default= 'p3',
        help_text='Clasificación por edad '

    )
   

    def __str__(self):
        return self.name 
    
    def get_absolute_url(self):
        return reverse('videojuegos-detail', args=[str(self.id)])

