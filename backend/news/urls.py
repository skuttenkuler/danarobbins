from django.urls import path, include
from . import views

urlpatterns = [
    path('api/news/', views.PostList.as_view() ),
]