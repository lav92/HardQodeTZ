from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework import generics

from datetime import datetime

from course.models import Product, Group, Lesson
from course.db_methods import invite_member
from course.serializers import ProductSerializer, ProductLessonsSerializer


def main(request):
    return HttpResponse('start study')


def invite(request, student_id, course_id):
    student = get_user_model().objects.get(pk=student_id)
    product = Product.objects.prefetch_related('group_product', 'students').get(pk=course_id)
    product.students.add(student)
    if not product.group_product.exists():
        Group.objects.create(title=f'{product.title}_group_1', product=product)
    invite_member(student, product)
    return render(request, 'course/invite.html')


class ProductsAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductLessonAPIView(generics.ListCreateAPIView):
    serializer_class = ProductLessonsSerializer

    def get_queryset(self):
        return Lesson.objects.filter(product__pk=self.kwargs['course_id'])
