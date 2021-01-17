from django.urls import path, include
from . import views

urlpatterns = [
    path('api/danarobbins/', views.GigList.as_view() ),
]