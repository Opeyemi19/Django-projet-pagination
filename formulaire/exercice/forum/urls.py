from django.urls import path
from .import views

urlpatterns = [
    path('', views.logins, name='conect'),
    path('regist', views.register, name='registe'),
    path('deconnect', views.deconnexion, name='deconnect'),
    path('dash', views.dashbord, name='homepage'),
]