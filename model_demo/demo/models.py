from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    birth_date = models.DateField()

class Card(models.Model):
    card_no = models.CharField(max_length=16)
    card_holder_name = models.CharField(max_length=100)
    cvv = models.CharField(max_length=3)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)