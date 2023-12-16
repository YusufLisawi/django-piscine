from django.urls import path
from . import views

urlpatterns = [
    path('populate', view=views.populate, name="ex03.populate"),
    path('display', view=views.display, name="ex03.display"),
]
