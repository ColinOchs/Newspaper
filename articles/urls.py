from django.urls import path

from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostDeleteView,
    PostUpdateView,
)

urlpatterns = [
    path('', PostListView.as_view(), name='article_list'),
    path('<int:pk>/', PostDetailView.as_view(), name= 'article_detail'),
    path('new/', PostCreateView.as_view(), name='article_new'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='article_delete'),
]