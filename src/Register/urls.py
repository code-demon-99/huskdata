from django.urls import path
from . import views
app_name="Register"
urlpatterns = [
    path('signup.php', views.signup, name='signup'),
]
