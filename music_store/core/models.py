from django.db import models
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError

from django.utils import timezone
from datetime import datetime

# Create your models here.


def validate_debut_year(year):
    current_year = timezone.now().year
    # if not (1 <= year <= current_year):
    if year not in range(1, current_year+1):
        raise ValidationError(f"Debut year must fall between 1 and {current_year}")
    

# def validate_release_date(release_date):
#     current_year = timezone.now().year
#     if release_date.year not in range(1800, current_year+1):
#         raise ValidationError(f"Release year must be between 1800 and {current_year}")

def validate_release_date(release_date):
    first_day_in_yr_1800 = datetime(1800, 1, 1)
    today = timezone.now()
    if release_date > today.date() or release_date < first_day_in_yr_1800.date():
    # if release_date not in range(1800, current_year+1):
        raise ValidationError(f"Release date must be between {first_day_in_yr_1800} and {today}")


class Artist(models.Model):
    name = models.CharField(max_length=100, validators=[MinLengthValidator(4)])
    debut_year = models.IntegerField(validators=[validate_debut_year])
    image = models.ImageField(upload_to='artist_images/', blank=True, null=True)

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=255, validators=[MinLengthValidator(2)])  # min length of 2
    release_date = models.DateField(validators=[validate_release_date])
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')
    cover_image = models.ImageField(upload_to='album_covers/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} by {self.artist}"