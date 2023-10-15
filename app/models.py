
from django.db import models
from django.contrib.auth.models import AbstractUser

#user
class ModelsUser(AbstractUser):
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'{self.username}'
    
#category
class ModelsCategory(models.Model):
    title = models.CharField('category name', max_length=15)
    owner = models.ForeignKey(ModelsUser, on_delete=models.CASCADE, related_name='owner')
    member = models.ManyToManyField(ModelsUser, related_name='member')
    start_date = models.DateField('start date', auto_now=True)
    end_date = models.DateField('end date')

    def __str__(self):
        return f'{self.title}'

#post
class ModelsPost(models.Model):
    title = models.TextField('post name', max_length=15)
    end_date = models.DateField('end date post', auto_now=True)
    post = models.ForeignKey(ModelsCategory, on_delete=models.CASCADE, related_name='post')
    assigned_to = models.ForeignKey(ModelsUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'
    