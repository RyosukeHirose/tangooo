from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser

class School(models.Model):
    school_name = models.CharField("school_name", max_length=50)

class Student(AbstractUser):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    
class WordCard(models.Model):
    card_name = models.CharField("card_name", max_length=30)
    subject = models.CharField("subject", max_length=50)
    school = models.ManyToManyField(School, verbose_name="school")
    question_id = models.IntegerField("question")
    correct_per = models.IntegerField("correct_per", validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)

class Qestion(models.Model):
    word_card = models.ManyToManyField(WordCard, verbose_name="card")
    front = models.CharField("front", max_length=256)
    back = models.CharField("back", max_length=256)
    correct_per = models.IntegerField("correct_per", validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
