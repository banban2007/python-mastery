from django.urls import path
from .views import *

urlpatterns = [
    path('hello/',hello),
    path('hello2/',hello2),
    path('hello3/<str:title>/',hello3),
    path('hello4/',hello4),
    path('hello5/',hello5),
]