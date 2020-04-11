from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser

class School(models.Model):
    school_name = models.CharField("school_name", max_length=50)

class Student(AbstractUser):
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('schoil_id', 0)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)
    
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
