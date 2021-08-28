from django.db import models
from django.contrib.auth import get_user_model
from django.urls.base import reverse


class Mentor(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.PROTECT,
        verbose_name="Пользователь",
    )

    status = models.CharField(
        max_length=200,
        default="",
        blank=True,
        verbose_name="Статус",
    )

    fullname = models.CharField(
        max_length=200,
        default='',
        blank=True,
        verbose_name="Полное имя",
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
        return f'{self.__class__.__name__} <{self.fullname}>'


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

    short_description = models.TextField(
        default="",
        blank=True,
        verbose_name="Описание курса",
    )

    full_description = models.TextField(
        default="",
        blank=True,
        verbose_name="Описание курса",
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курс"

    def __str__(self):
        return f"{self.__class__.__name__} <{self.title}>"


class Student(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.PROTECT,
        verbose_name="Пользователь",
    )

    status = models.CharField(
        max_length=200,
        default="",
        blank=True,
        verbose_name="Статус",
    )

    fullname = models.CharField(
        max_length=200,
        default='',
        blank=True,
        verbose_name="Полное имя",
    )

    bio = models.TextField(
        default="",
        blank=True,
        verbose_name="Биография",
    )

    courses = models.ManyToManyField(
        Course,
        blank=True,
        related_name="students",
        verbose_name="Курсы",
    )

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"

    def __str__(self):
        return f"{self.__class__.__name__} <{self.fullname}>"