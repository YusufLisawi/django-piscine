from django.urls import path

from . import views

urlpatterns = [
    path('django', view=views.django, name='django'),
    path('display', view=views.display, name='display'),
    path('templates', view=views.templates, name='templates'),
]
