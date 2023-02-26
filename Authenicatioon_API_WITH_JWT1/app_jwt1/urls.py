from django.urls import path
from app_jwt1.views import *
urlpatterns = [
    path('register/',UserRegistionView.as_view()),
    path('login/',UserLoginView.as_view())
]
