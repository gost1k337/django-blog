from django.shortcuts import render
from .models import Account
from django.views.generic import View, TemplateView
from .forms import RegisterForm


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'account/register.html', {'form': form})


class LoginView(TemplateView):
    template_name = 'account/login.html'
