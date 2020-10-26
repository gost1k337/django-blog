from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import View, FormView
from .forms import RegisterForm, LoginForm


class RegisterView(View):
    @staticmethod
    def get(request):
        if request.user.is_authenticated:
            return redirect('blog:home')
        form = RegisterForm()
        return render(request, 'account/register.html', {'form': form})

    @staticmethod
    def post(request):
        context = {}
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            if user is not None:
                return redirect('blog:home')
        context['form'] = form
        return render(request, 'account/register.html', context)


class LoginView(View):
    @staticmethod
    def get(request):
        if request.user.is_authenticated:
            return redirect('blog:home')
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})

    @staticmethod
    def post(request):
        context = {}
        form = LoginForm(request.POST)
        if form.is_valid():
            credentials = form.cleaned_data
            user = authenticate(username=credentials['email'],
                                password=credentials['password'])
            if user is not None:
                login(request, user)
                return redirect('blog:home')
        context['form'] = form
        return redirect('account:login')


def LogoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('account:login'))
