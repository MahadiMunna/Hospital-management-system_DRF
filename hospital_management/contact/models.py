from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=14)
    problem = models.TextField()

    def __str__(self) -> str:
        return f'{self.name} - {self.problem}'
    
    class Meta:
        verbose_name_plural = 'Contact Us'