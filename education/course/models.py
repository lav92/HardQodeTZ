from django.db import models
from django.contrib.auth import get_user_model


class Product(models.Model):
    title = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    max_students_in_group = models.IntegerField(blank=True, default=30)
    min_students_in_group = models.IntegerField(blank=True, default=5)

    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name='author_courses')
    students = models.ManyToManyField(get_user_model(), blank=True, related_name='product_students')

    objects = models.Manager()

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=255)

    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='lesson_product')

    objects = models.Manager()


class Group(models.Model):
    title = models.CharField(max_length=255)

    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='group_product')
    students = models.ManyToManyField(get_user_model(), blank=True, related_name='group_students')

    objects = models.Manager()

    def __str__(self):
        return f'{self.title} length={len(self.students.all())}'

    def __len__(self):
        return len(self.students.all())
