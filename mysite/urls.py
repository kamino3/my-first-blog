
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('contact/', include('contact.urls')),
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('login/', RedirectView.as_view(url='/accounts/login/'), name='login-redirect'),
        path('accounts/', include('allauth.urls')),
]
