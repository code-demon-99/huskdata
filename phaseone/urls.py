from django.urls import path
from . import views
    
app_name = "phaseone"
urlpatterns = [
    path("", views.home_view, name='home'),
    path("signin", views.login, name="login"),
    path('signup.php', views.signup, name='signup'),
    path("home", views.home_view, name='home'),
]
