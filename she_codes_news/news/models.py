from django.contrib.auth import get_user_model
from django.db import models

# class Category(models.Model):
#     name = models

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    # author = models.CharField(max_length=200)
    author=models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    
    pub_date = models.DateTimeField()
    image = models.URLField(blank=True) 
    content = models.TextField()
    # category = models.CharField(max_length=225,)
    
    class Meta: 
        ordering = ['-pub_date']


