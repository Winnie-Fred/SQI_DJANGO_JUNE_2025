import os

from collections import Counter

from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.template.defaultfilters import slugify
from django.utils import timezone


User = get_user_model()


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField()
    year_of_birth = models.DateField()
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class GenreChoices(models.TextChoices):
    FANTASY = "FTSY", "Fantasy"
    SCI_FI = "SCIFI", "Science Fiction"
    MYSTERY_THRILLER = "MYST_THRILL", "Mystery/Thriller"
    ROMANCE = "ROM", "Romance" 
    HISTORICAL_FICTION = "HIST_FIC", "Historical Fiction"
    HORROR = "HORROR", "Horror"
    DYSTOPIAN = "DYST", "Dystopian"
    ADVENTURE = "ADVN", "Adventure"
    BIO_AUTOBIO = "BIO_AUTOBIO", "Biography/Autobiography"
    SELF_HELP = "SELF_HELP", "Self Help"
    HISTORY = "HIST", "History"
    SCIENCE = "SCI", "Science"
    BUSINESS = "BSNS", "Business"


def book_cover_upload_to(instance, filename):
    # Generate a shorter, more manageable file name
    _, ext = os.path.splitext(filename)
    return f"book_cover_images/{slugify(instance.title)}{ext}"

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    genre = models.CharField(max_length=11, choices=GenreChoices.choices, default=GenreChoices.FANTASY)
    publication_date = models.DateField()
    cover_image = models.ImageField(upload_to=book_cover_upload_to, default="default-cover.jpg")
    isbn = models.CharField(max_length=15)
    number_of_pages = models.PositiveIntegerField()
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} by {self.author}"
    

    def calculate_avg_rating(self):
        total_rating = 0
        all_reviews = self.review_set.all()
        for review in all_reviews:
            total_rating += review.rating
        no_of_ratings = len(all_reviews)
        if not no_of_ratings:
            return 0
        avg_rating = total_rating / no_of_ratings
        return round(avg_rating, 1)

    def get_rating_distribution(self):
        all_reviews = self.review_set.all()
        # all_ratings = []
        # for review in all_reviews:
        #     rating = review.rating
        #     all_ratings.append(rating)

        all_ratings = [review.rating for review in all_reviews]
        ratings_distribution = Counter(all_ratings)

        distribution = {5:0, 4: 0, 3: 0, 2: 0, 1: 0}

        for rating, occurence in ratings_distribution.items():
            distribution[rating] = round((occurence / len(all_ratings)) * 100)
        return distribution




class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    comment = models.TextField()
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], help_text="Rating must be between 1 and 5.")

    def __str__(self):
        return f"Review by {self.added_by} on {self.book}"
    
    def added_since(self):
        today = timezone.now()
        days_since_added = today - self.added_on
        days_since_added = days_since_added.days
        return days_since_added
    
    def can_still_edit(self):
        today = timezone.now()
        five_minutes = timezone.timedelta(minutes=5)
        return today - self.added_on <= five_minutes
            