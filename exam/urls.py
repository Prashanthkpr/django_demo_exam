from django.contrib import admin
from django.urls import path
from exam.views import *


app_name = 'exam'

urlpatterns = [
    path('home/', home, name='home'),
    path('contact/', contact, name="contact"),
    path('about/', about, name="about"),
    path('questions/list/', questions_list, name="questions_list"),
    path('question/<int:id>/delete/', delete_question, name="delete_question"),
    path('questions/create/', create_question, name="create_question"),
    path('question/<int:id>/update/', update_question, name="update_question"),
]
