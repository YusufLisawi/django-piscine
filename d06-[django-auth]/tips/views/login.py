from pyexpat.errors import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

class LoginFormView(LoginView):
    template_name = "auth/login.html"
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.warning(request, "You are already logged in")
            return redirect('index')
        return super().get(request, *args, **kwargs)
    
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            messages.success(self.request, "You have successfully logged in")
            return redirect('index')
        return super().form_valid(form)