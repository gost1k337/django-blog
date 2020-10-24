from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import View, FormView
from .forms import RegisterForm, LoginForm


class RegisterView(View):
    @staticmethod
    def get(request):
        form = RegisterForm()
        return render(request, 'account/register.html', {'form': form})

    @staticmethod
    def post(request):
        context = {}
        form = RegisterForm(request.POST)
        print(form.fields)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            if user is not None:
                return redirect('blog:home')
        context['form'] = form
        return render(request, 'account/register.html', context)


class LoginView(FormView):
    form_class = LoginForm
    success_url = reverse_lazy('blog:home')
    template_name = 'account/login.html'

    def form_valid(self, form):
        print('form_valid', 'True')
        credentials = form.cleaned_data

        user = authenticate(email=credentials['email'],
                            password=credentials['password'])

        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect(self.success_url)

        return HttpResponseRedirect(reverse_lazy('account:login'))


def LogoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('account:login'))
