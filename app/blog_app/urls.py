from django.urls import path
from .views import HomeView, ProfileView

app_name = 'blog'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
