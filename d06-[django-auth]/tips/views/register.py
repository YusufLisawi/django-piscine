from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from ..forms import RegisterForm
from django.views.generic import FormView
from django.contrib.auth import login
from django.contrib import messages

class RegisterFormView(FormView):
    template_name = "auth/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.warning(request, "You are already logged in")
            return redirect('index')
        return super().get(request, *args, **kwargs)
    
    def form_valid(self, form) -> HttpResponse:
        user = form.save()
        login(self.request, user)
        if self.request.user.is_authenticated:
            messages.success(self.request, "You have successfully registered")
            return redirect('index')
        return super().form_valid(form)
    
    def form_invalid(self, form) -> HttpResponse:
        if self.request.user.is_authenticated:
            messages.warning(self.request, "You are already logged in")
            return redirect('index')
        return super().form_invalid(form)