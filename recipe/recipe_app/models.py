from django.db import models

from django.core.validators import MinValueValidator


# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.TextField(help_text="Comma-separated ingredients")
    instructions = models.TextField(help_text="Numbered list of instructions")
    cooking_time = models.IntegerField(validators=[MinValueValidator(3)])
    image = models.ImageField(upload_to="recipe_images/")
    cover_image = models.ImageField(upload_to="recipe_covers/", default="defaults/default-recipe-cover.jpg")