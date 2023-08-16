
# urls.py: このファイルではアプリケーションのURLパターンが定義されています。
# 各URLパターンは、リクエストを処理するビューと関連付けられています。
# URLパターンは動的な部分（例：<int:pk>）を含むことができ、URLから値をキャプチャします。

from .views import SearchResultsView
from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView


urlpatterns = [
path('accounts/profile/', views.profile_view, name='profile_view'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    

    path('exam/', views.exam, name='exam'),

    path('account_info/', views.account_info, name='account_info'),
]

from django.contrib.auth.views import LogoutView

urlpatterns.append(path('accounts/logout/', LogoutView.as_view(), name='logout'))
