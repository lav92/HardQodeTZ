from rest_framework.serializers import ModelSerializer

from course.models import Product, Lesson


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'start_date']


class ProductLessonsSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['title', 'url']
