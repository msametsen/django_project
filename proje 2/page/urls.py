
from django.urls import path
from .views import (
    home_view,
    contact_us_view,
    about_us_view,
    vizion_view
)

urlpatterns = [
    path('about_us/', about_us_view, name='about_us'),
    path('contact/', contact_us_view, name='contact_us'),
    path('vision/', vizion_view, name='vision'),
    path('', home_view, name='home'),
]
