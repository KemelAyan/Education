from django.urls import path

from .views import *

urlpatterns = [
    path('',index),
    path('ru/',zayavka),
    path('zayavkakz/',zayavkaKz),
    path('zayavkaru/',zayavkaRu),
]