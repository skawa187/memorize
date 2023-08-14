from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=20, null=False, blank=False)
    description=models.TextField(null=True)

    def __str__(self) -> str:
        return self.name

class Memo(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    body = models.TextField(null=True, blank=True)
    importance = models.PositiveIntegerField(blank = True, default=0)
    category = models.ForeignKey(Category, blank=False, on_delete=models.SET_DEFAULT, default=0)
    created = models.DateTimeField(auto_now_add=True)
    edited_last = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['-edited_last']
        db_table_comment = 'Table created by Django'

