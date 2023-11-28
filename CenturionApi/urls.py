from django.urls import path
from CenturionApi import views


urlpatterns = [
    path('signin/', views.SignIn.as_view(), name='signin')
]