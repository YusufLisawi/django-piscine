from django.urls import path
from . import views

urlpatterns = [
    path('populate', view=views.populate, name="ex05.populate"),
    path('display', view=views.display, name="ex05.display"),
    path('remove', view=views.remove, name="ex05.remove"),
]
