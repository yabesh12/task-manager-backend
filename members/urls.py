from django.urls import path
from .views import UserSignupView, UserLoginView, UserLogoutView

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='user_signup'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'),
]
