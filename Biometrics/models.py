from django.db import models
from django.contrib import admin

# Create your models here.


from django.db import models

class Student(models.Model):
    REGISTRATION_NUMBER_MAX_LENGTH = 20

    student_id = models.CharField(max_length=REGISTRATION_NUMBER_MAX_LENGTH, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    left_index_finger_data = models.TextField(blank=True, null=True)
    right_index_finger_data = models.TextField(blank=True, null=True)
    student_number = models.CharField(max_length=20, unique=True)
    programme = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='media/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.student_id})"




admin.site.register(Student)