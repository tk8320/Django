from django.db import models

# Create your models here.

gender_choice = [
        ('M', "Male"),
        ('F', "Female"),
        ('U', "Undefined")
    ]


class Class(models.Model):
    def __str__(self):
        return f"<{self.class_id}-{self.class_name}>"

    class_id = models.IntegerField(primary_key=True)
    class_name = models.CharField(max_length=100,null=False)
    class_teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)


class Teacher(models.Model):
    def __str__(self):
        return f"<{self.teacher_id}-{self.name}>"

    teacher_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, null=False, verbose_name="Teacher Name")
    age = models.IntegerField(null=False)
    gender = models.CharField(choices=gender_choice, max_length=50)


class Student(models.Model):
    def __str__(self):
        return f"<{self.student_id}-{self.name}>"

    student_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, null=False)
    age = models.IntegerField(null=False)
    gender = models.CharField(max_length=100,default="Undefined", choices=gender_choice)
    c_no = models.DecimalField(max_digits=10, decimal_places=0,verbose_name="Contact Number")
    teacher = models.ManyToManyField(to=Teacher)

