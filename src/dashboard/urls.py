from django.urls import path
from . import views
app_name = "dashboard"
urlpatterns = [
    path("welcome.php",views.dashboard_view,name='dashboard'),
]
