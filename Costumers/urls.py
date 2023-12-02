from django.urls import path
from django.contrib.auth.decorators import login_required

from Costumers import views

compilance = login_required(views.Compilance.as_view())
lessors = login_required(views.Lessors.as_view())

urlpatterns = [
    path('compilance/', compilance, name='compilance'),
    path('lessors/', lessors, name='lessors'),
]