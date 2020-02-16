from django.urls import path
from aboutus.views import *;
app_name = "aboutus"
urlpatterns = [
    path("aboutus",aboutus,name='about'),
    path("aboutus/rishi",portone,name='rishi'),
    path("aboutus/sumit",porttwo,name='sumit'),
    path("aboutus/ritika",portthree,name='ritika'),
]
