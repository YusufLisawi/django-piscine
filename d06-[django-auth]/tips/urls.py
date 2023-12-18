
from .views import views, register, logout, login
from django.urls import path

urlpatterns = [
    path('', view=views.index, name='index'),
    path('register', register.RegisterFormView.as_view(), name='register'),
    path('login', login.LoginFormView.as_view(), name='login'),
    path('logout', view=logout.logout_view, name='logout')
]
