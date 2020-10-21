from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('blog/', include('blog_app.urls')),
    path('accounts/', include('account.urls')),
    path('admin/', admin.site.urls),
]
