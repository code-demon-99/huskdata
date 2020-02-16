from django.urls import path
from . import views
app_name = "phaseone"
urlpatterns = [
    path("", views.home_view, name='home'),
    path("signin", views.login, name="login"),
    path('signup.php', views.signup, name='signup'),
    path("aboutus", views.aboutus, name='about'),
    path("aboutus/rishi", views.portone, name='rishi'),
    path("aboutus/sumit", views.porttwo, name='sumit'),
    path("aboutus/ritika", views.portthree, name='ritika'),
]
