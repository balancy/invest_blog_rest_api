# Generated by Django 3.2.6 on 2021-08-23 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0005_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(blank=True, related_name='students', to='education.Course', verbose_name='Курсы'),
        ),
    ]
