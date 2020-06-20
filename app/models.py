from django.db import models
from django.utils.timezone import datetime

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    mobile = models.PositiveIntegerField(default=880)
    gradation = models.PositiveIntegerField()
    designation = models.CharField(max_length=50)
    posting = models.CharField(max_length=200)
    gender = models.CharField(max_length=50, choices=(
        ('male', 'Male'),
        ('female', 'Female')
    ))
    image = models.ImageField(upload_to='images/', blank=True)
    date_added = models.DateField(default=datetime.now)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-id']