
from django.urls import path

from . import views

urlpatterns = [

    path('', views.PostListView.as_view(), name='post_page'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail_page'),
    path('create/', views.PostCreateView.as_view(), name='new_page'),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='update_page'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete_page'),
]
