from django.db import models

class Employee(models.Model):
    emp_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    experience = models.IntegerField()
    image = models.ImageField(upload_to='employees/', blank=True, null=True)

    def __str__(self):
        return f"{self.emp_id} - {self.name}"
