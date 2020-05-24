from django.urls import path
from . import views
app_name = "phasetwo"
urlpatterns = [
    path('welcome', views.welcome, name='welcome'),
    path('page2', views.page2, name='page2'),
    path('logout', views.logout_view, name='logout'),
    path('page3', views.page3, name='page3'),
    path('export',views.page5,name='page5')
]
