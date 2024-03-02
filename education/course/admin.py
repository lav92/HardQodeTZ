from django.contrib import admin
from django.contrib.admin import register

from course.models import Product, Lesson, Group

# password for all students - lobanav1907

@register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'start_date', 'author')


@register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'url', 'product')


@register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'product')
