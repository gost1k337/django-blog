from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('blog_app.urls')),
    path('accounts/', include('account.urls')),
    path('admin/', admin.site.urls),
]
