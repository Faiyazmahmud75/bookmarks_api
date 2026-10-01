from django.db import models

class Bookmark(models.Model):
    title = models.CharField(max_length=30)
    url = models.URLField(max_length=500)
    description = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title