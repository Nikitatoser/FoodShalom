from django.db import models

class Person(models.Model):
    title = models.CharField('Назва', max_length = 50)
    full_text = models.TextField('Text')
    education = models.CharField('Назва', max_length = 50)
    full_text_one = models.TextField('Text')
    ability = models.CharField('Назва', max_length = 50)
    full_text_two = models.TextField('Text')
    usfoto = models.ImageField(upload_to='images/', blank=True, null=True)
    
def __str__(self):
        return self.title

class Meta:
    verbose_name = 'Користувач'
    verbose_name_plural = 'Користувачі'
    

from portfolio.models import Articles
from django.db import models

class Rates(models.Model):
    article = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name='rates')
    username = models.CharField('Username', max_length=150)
    rating = models.PositiveIntegerField('Rating', default=0)
    comment = models.TextField('Comment', blank=True, null=True)
    created_at = models.DateTimeField('Created At', auto_now_add=True)

    def __str__(self):
        return f'{self.article.title} - {self.rating} by {self.username}'

    class Meta:
        verbose_name = 'Rate'
        verbose_name_plural = 'Rates'


