from django.urls import path
from . import views

urlpatterns = [
    path('init', view=views.init, name="ex00.init")
]
