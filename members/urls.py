from django.urls import path
from .views import CurrentUserView, UserSignupView, UserLoginView, UserLogoutView

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='user_signup'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('me/', CurrentUserView.as_view(), name='current_user'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'),
]
