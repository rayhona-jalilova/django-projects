from django.db import models

# Create your models here.

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=60)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Blog {self.title}"