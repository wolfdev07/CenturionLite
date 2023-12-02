from django.urls import path
from django.contrib.auth.decorators import login_required

from Costumers import views

costumers = login_required(views.Costumers.as_view())

urlpatterns = [
    path('compilance/', costumers, name='costumers'),
]