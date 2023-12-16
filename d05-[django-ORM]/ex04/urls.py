from django.urls import path
from . import views

urlpatterns = [
    path('init', view=views.init, name="ex04.init"),
    path('populate', view=views.populate, name="ex04.populate"),
    path('display', view=views.display, name="ex04.display"),
    path('remove', view=views.remove, name="ex04.remove"),
]
