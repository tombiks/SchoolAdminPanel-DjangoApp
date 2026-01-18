from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator

# Create your models here.

class Student(models.Model):
    no=models.IntegerField(validators=[MinValueValidator(1000), MaxValueValidator(9999)], unique=True, null=False)
    name=models.CharField(max_length=50, validators=[MinLengthValidator(3)], null=False)
    surname=models.CharField(max_length=50, validators=[MinLengthValidator(3)], null=False)
    birthDate=models.DateField(null=False)
    section=models.ForeignKey('Section', on_delete=models.CASCADE, related_name='students', null=False)   

    def __str__(self):
        return f"{self.no} - {self.name} {self.surname}"

class Teacher(models.Model):    
    name=models.CharField(max_length=50, validators=[MinLengthValidator(3)], null=False)
    surname=models.CharField(max_length=50, validators=[MinLengthValidator(3)], null=False)    
    birthDate=models.DateField(null=False)
    lesson=models.ForeignKey('Lesson', on_delete=models.CASCADE, related_name='teachers', null=False)

    def __str__(self):
        return f"{self.name} {self.surname}"
    
class Section(models.Model):
    grade=models.IntegerField(max_length=1, null=False)
    branch=models.CharField(max_length=1, null=False)

    def __str__(self):
        return f"{self.grade}/{self.branch}"
    
class Lesson(models.Model):
    name=models.CharField(max_length=50, validators=[MinLengthValidator(3)], null=False)    

    def __str__(self):
        return f"{self.name}"
    
class Notes(models.Model):    
    firstQuiz=models.FloatField()
    secondQuiz=models.FloatField()
    finalExam=models.FloatField() 
    @property
    def avarage(self):
        return (self.firstQuiz*0.3 + self.secondQuiz*0.3 + self.finalExam*0.4)
    
    student=models.ForeignKey('Student', on_delete=models.CASCADE, related_name='notes', null=False)
    lesson=models.ForeignKey('Lesson', on_delete=models.CASCADE, related_name='notes', null=False)
    
    def __str__(self):
        return f"{self.student} - {self.lesson}: {self.firstQuiz}, {self.secondQuiz}, {self.finalExam}, {self.avarage:.2f}"
    

