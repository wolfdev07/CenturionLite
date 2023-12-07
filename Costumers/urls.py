from django.urls import path
from django.contrib.auth.decorators import login_required

from Costumers import views

compilance = login_required(views.Compilance.as_view())
profile = login_required(views.ProfileUser.as_view())
lessors = login_required(views.Lessors.as_view())
ConcurrentAddress = login_required(views.ConcurrentAddress.as_view())
propertyDetails = login_required(views.CreateLeaseProperty.as_view())

urlpatterns = [
    path('compilance/', compilance, name='compilance'),
    path('profile/', profile, name="profile_costumer" ),
    path('lessors/', lessors, name='lessors'),
    path('address/', ConcurrentAddress, name='addres_costumer'),
    path('create/lease/property/', propertyDetails, name='lease_property_details')
]