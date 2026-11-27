from django.db import models
from shared.models import TimeStampMixin
from django.core.validators import MinValueValidator, MaxValueValidator



class Student(TimeStampMixin):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    age = models.IntegerField(
        validators=[MinValueValidator(3), MaxValueValidator(30)]
    )
    
    department = models.CharField(max_length=100)
    