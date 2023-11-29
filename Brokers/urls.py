from django.urls import path
from django.contrib.auth.decorators import login_required

from Brokers import views

dashboard = login_required(views.Dashboard.as_view())

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),

]