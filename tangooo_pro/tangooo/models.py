from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, school_id, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            school_id=school_id
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password, school_id):
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
            school_id=school_id
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class School(models.Model):
    school_name = models.CharField("school_name", max_length=50)

    def __str__(self):
        return self.school_name

class Student(AbstractUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth', 'school_id']

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    
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
