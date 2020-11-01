from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model


class HomeView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'

    def get(self, request):
        return render(request, 'blog_app/home_page.html')


class ProfileView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'

    def get(self, request):
        # User = get_user_model()
        context = {}
        user = request.user
        context['user'] = user
        context['followers'] = user.followers.all()[:5]
        return render(request, 'blog_app/profile_page.html', context=context)
