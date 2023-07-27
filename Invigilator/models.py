from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from Biometrics.models import Student
from Admin.models import AdminUser

 

class Invigilator(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100,null=True, blank=True)
    last_name = models.CharField(max_length=100,null=True, blank=True)
    added_by = models.ForeignKey(AdminUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='added_invigilators')
    # Use 'related_name' to specify a custom reverse accessor name for the ForeignKey

    # Add any other fields specific to the Invigilator model here

    def __str__(self):
        return f"{self.first_name} {self.last_name}"







class Exam(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    assigned_invigilator = models.ForeignKey(Invigilator, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name

class ExamInvigilator(models.Model):
    invigilator = models.ForeignKey(Invigilator, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.invigilator.user.username} - {self.exam.name}"

class ExamRoom(models.Model):
    room_number = models.CharField(max_length=10, unique=True)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"Room {self.room_number} (Capacity: {self.capacity})"

class ExamAssignment(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    invigilator = models.ForeignKey(Invigilator, on_delete=models.CASCADE)
    exam_room = models.ForeignKey(ExamRoom, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.invigilator.user.username} - {self.exam.name} - Room {self.exam_room.room_number}"



admin.site.register(Invigilator)
admin.site.register(Exam)
admin.site.register(ExamInvigilator)
admin.site.register(ExamRoom)
