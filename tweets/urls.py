from django.urls import path
from . import views


urlpatterns = [
    path('tweets/', views.TweetAV.as_view(), name='tweet-list'),
    path('tweets/<int:pk>/', views.TweetDetailAV.as_view(), name='tweet-detail'),
]