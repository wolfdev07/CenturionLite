from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from django.urls import path
from CenturionApi import views
from CenturionApi import api


urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.SignIn.as_view(), name='signin'),
    path('logout/', views.signout, name='logout'),
    # API URLS
    path(r'api/get-postal-code/<code>/', api.get_postal_code, name='get_postalcode'),
]

urlpatterns = format_suffix_patterns(urlpatterns)