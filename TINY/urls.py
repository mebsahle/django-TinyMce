from django.urls import include, path
from .import views
app_name = "TINY"
urlpatterns = [
    path('', views.home, name='home'),
    path('register/',views.register,name='register'),
]