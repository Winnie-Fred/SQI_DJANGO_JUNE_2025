from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

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
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} by {self.added_by}"