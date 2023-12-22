from django.urls import path
from django.contrib.auth.decorators import login_required

from LegalServices import views

manager = login_required(views.ManagerView.as_view())


urlpatterns = [
    path('manager/', manager, name='manager'),
]