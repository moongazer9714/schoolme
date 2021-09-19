from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post_detail/', views.post_detail, name='post_detail'),
    path('student/', views.student, name='student'),
    path('teacher/', views.teacher, name='teacher'),
    path('admins/', views.admins, name='admins'),
    path('contact/', views.contactus, name='contactus'),
    path('aboutus/', views.aboutus, name='aboutus'),
    ]