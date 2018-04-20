from django.db import models
from django.urls.base import reverse

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 100)#博客题目
    category = models.CharField(max_length = 50)#博客标签
    date_time = models.DateTimeField(auto_now_add=True)#博客日期
    content = models.TextField(blank=True,null=True) #博客文章正文
    
    def get_absolute_url(self):
        path = reverse('detail',kwargs={'id':self.id})
        return "http://127.0.0.1:9999%s"%path
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date_time']
