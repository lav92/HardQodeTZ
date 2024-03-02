from django.urls import path

from course.views import main, invite, ProductsAPIView, ProductLessonAPIView

app_name = 'course'

urlpatterns = [
    path('home/', main, name='index'),
    path('invite/<int:student_id>/<int:course_id>/', invite, name='invite'),
    # <-------------------API---------------->
    path('api/all_products/', ProductsAPIView.as_view()),
    path('api/product_lessons/<int:course_id>/', ProductLessonAPIView.as_view())
]
