# Generated by Django 4.1.7 on 2023-03-10 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_teacher_alter_student_c_no_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='teacher_name',
            field=models.ManyToManyField(to='students.teacher'),
        ),
    ]
