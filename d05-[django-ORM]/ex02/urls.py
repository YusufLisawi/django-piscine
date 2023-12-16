from django.urls import path
from . import views

urlpatterns = [
    path('init', view=views.init, name="ex02.init"),
    path('populate', view=views.populate, name="ex02.populate"),
    path('display', view=views.display, name="ex02.display"),
]
