from django.urls import path
from . import views

urlpatterns = [
    path('display', view=views.display),
]
