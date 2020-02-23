from django.urls import path
from . import views
app_name = "phasetwo"
urlpatterns = [
    path('welcome',views.welcome,name = 'welcome')
]
