# Generated by Django 3.2.6 on 2021-08-18 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_mentor_fullname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='fullname',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Полное имя'),
        ),
    ]
