# Generated by Django 3.2.6 on 2021-08-18 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentor',
            name='fullname',
            field=models.TextField(blank=True, default='', verbose_name='Полное имя'),
        ),
    ]