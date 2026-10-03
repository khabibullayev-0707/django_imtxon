from django.db import models
class Student(models.Model):
    ism=models.CharField(max_length=100)
    yosh=models.PositiveIntegerField()
    kurs=models.PositiveIntegerField()
    def __str__(self): return self.ism
class Reja(models.Model):
    sarlavha=models.CharField(max_length=200)
    batafsil=models.TextField(blank=True)
    sana=models.DateField()
    bajarildi=models.BooleanField(default=False)
    student=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='rejalar')
    def __str__(self): return self.sarlavha
