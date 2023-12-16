from django.urls import path
from . import views

urlpatterns = [
    path('init', view=views.init, name="ex08.init"),
    path('populate', view=views.populate, name="ex08.populate"),
    path('display', view=views.display, name="ex08.display"),
]
