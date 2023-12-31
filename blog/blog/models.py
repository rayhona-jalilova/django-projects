from django.db import models
from django.urls import reverse 
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=60)
    description = models.TextField(blank=True, null=True)
    author = models.ForeignKey(
        'auth.User',
        on_delete = models.CASCADE
    )
    
    
    def __str__(self):
        return f"{self.title}"
    
    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.pk)])
    