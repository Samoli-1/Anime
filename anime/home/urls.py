from django.urls import path
from home import views

app_name = 'home'  # namespace for URL names

urlpatterns = [
    path('', views.Home, name='index'),  # root URL ('/') pe Home view chalega
]
