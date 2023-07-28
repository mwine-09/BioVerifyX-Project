from django.db import models
from Admin.models import User

 
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

class StudentManager(models.Manager):
    # function that returns all students
    def get_all_students(self):
        return self.all()
        

class Student(models.Model):
    studentNumber = models.IntegerField(primary_key=True, unique=True)
    registrationNumber = models.CharField(max_length=15)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    left_index_finger_data = models.TextField(blank=True, null=True)
    right_index_finger_data = models.TextField(blank=True, null=True)
    program = models.CharField(max_length=100)
    biometrics = models.BinaryField(null=True, blank=True, editable=True)
    profilePhoto = models.ImageField(
        upload_to='profile_photos/', default=get_default_profile_photo)
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        default='Male',
    )
    YEAR_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    ]
    year = models.CharField(
        max_length=1,
        choices=YEAR_CHOICES,
        default='1',
    )
    RETAKE_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    retake = models.CharField(
        max_length=3,
        choices=RETAKE_CHOICES,
        default='no',
    )
    courseCode = models.ForeignKey(CourseUnit, on_delete=models.CASCADE)
    adminNumber = models.ForeignKey(Administrator, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.firstName} {self.lastName} (Student Number: {self.studentNumber})'
 