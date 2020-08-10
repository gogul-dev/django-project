from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    text = models.TextField()
    created_date = models.DateField(auto_now=True)
    published_date = models.DateField(null=True,blank=True)

    def publish(self):
        self.publish_date = timezone.now
        self.save

    def __str__(self):
        return self.title
    