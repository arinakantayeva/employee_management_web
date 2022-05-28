from django.urls import path
from . import views
from .views import SignUpView

urlpatterns = [
    path('login', views.login_user, name="login"),
    path('logout', views.logout_user, name="logout"),
    path('signup', SignUpView.as_view(), name="signup")
]
