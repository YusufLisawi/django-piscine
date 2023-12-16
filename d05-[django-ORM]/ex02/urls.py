from django.urls import path
from . import views

urlpatterns = [
    path('init', view=views.init, name="init"),
    path('populate', view=views.populate, name="populate"),
    path('display', view=views.display, name="display"),
]
