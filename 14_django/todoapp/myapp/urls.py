from django.urls import path
from .views import *

urlpatterns = [
    path('create/',Create),
    path('',List),
    path('delete/<int:tid>/',Delete),
    path('details/<int:tid>/',Details)
]