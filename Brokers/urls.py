from django.urls import path
from django.contrib.auth.decorators import login_required

from Brokers import views

dashboard = login_required(views.Dashboard.as_view())
costumer_details=login_required(views.CostumerDetails.as_view())

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('details/<membership>/', costumer_details, name="costumer_details"),
]