from django.urls import path
from CenturionApi import views


urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.SignIn.as_view(), name='signin'),
    path('logout/', views.signout, name='logout'),
]