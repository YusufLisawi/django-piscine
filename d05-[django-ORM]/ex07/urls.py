from django.urls import path
from . import views

urlpatterns = [
    path('populate', view=views.populate, name="ex07.populate"),
    path('display', view=views.display, name="ex07.display"),
    path('update', view=views.update, name="ex07.update"),
]
