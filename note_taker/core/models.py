from django.db import models

# Create your models here.

class Category(models.TextChoices):
    PERSONAL = "PSNL", "Personal"
    WORK = "WK", "Work"
    IDEAS = "IDE", "Ideas"


class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.CharField(choices=Category.choices, max_length=4, default=Category.PERSONAL)
    created_at = models.DateTimeField(auto_now_add=True)