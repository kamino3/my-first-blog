from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.post_list, name='post_list'),
]
from . import views

urlpatterns += [
    path('new/', views.new_article, name='new_article'),
]
