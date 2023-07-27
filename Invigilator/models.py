from django.db import models
from Admin.models import User



from Biometrics.models import Student




# Create your models here.
 
class Invigilator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    assigned_exams = models.ManyToManyField('Exam', through='ExamInvigilator')


    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username








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