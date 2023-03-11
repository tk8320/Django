# Generated by Django 4.1.7 on 2023-03-10 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_student_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='Teacher Name')),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('U', 'Undefined')], max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='c_no',
            field=models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Contact Number'),
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('class_id', models.IntegerField(primary_key=True, serialize=False)),
                ('class_name', models.CharField(max_length=100)),
                ('class_teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.teacher')),
            ],
        ),
    ]
