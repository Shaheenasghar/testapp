from django.db import models
from unittest.util import _MAX_LENGTH

class BSIT(models.Model):
    Class_Teacher = models.CharField(max_length=1000)
    Class_Title = models.CharField(max_length=500)
    University = models.CharField(max_length=500)
    Class_Logo = models.CharField(max_length=500)
    
    def __str__(self):
        return self.Class_Title + '-' + self.Class_Teacher

class Students(models.Model):
    bsit = models.ForeignKey(BSIT, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    student_Name = models.CharField(max_length=20)
    