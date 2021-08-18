from django.db import models
from django.contrib.auth.models import User


class Mentor(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        verbose_name="Пользователь",
    )

    status = models.CharField(
        max_length=200,
        default="",
        blank=True,
        verbose_name="Статус",
    )

    bio = models.TextField(
        default='',
        blank=True,
        verbose_name="Биография",
    )

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'

    def __str__(self):
        return f'{self.__class__.__name__} <{self.user}>'


class Course(models.Model):
    mentor = models.ForeignKey(
        Mentor,
        on_delete=models.PROTECT,
        verbose_name="Ментор",
        related_name="courses",
    )

    title = models.CharField(
        max_length=150,
        default="",
        verbose_name="Название",
    )

    description = models.TextField(
        default="",
        blank=True,
        verbose_name="Описание курса",
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курс"

    def __str__(self):
        return f"{self.__class__.__name__} <{self.title}>"
