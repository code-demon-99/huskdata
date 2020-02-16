from django.urls import path
from . import views
app_name="login"
urlpatterns = [
    path("signin.php",views.login_view,name="login"),
    #path("logout", views.logout_view, name="logout"),
    path("auth", views.check_login, name="auth"),
    
    ]

