# service_requests/urls.py

from django.urls import path
from . import views
from .views import user_page
from .views import CustomLoginView
from .views import submit_request
from .views import register_customer

urlpatterns = [
    path('submit/', views.submit_request, name='submit_request'),
    path('track/', views.track_request, name='track_request'),
    path('account/', views.account_info, name='account_info'),
    path('/home', views.home, name='home'),
    path('user/', user_page, name='user_page'),
    path('', CustomLoginView.as_view(), name='login'),
    path('register/', register_customer, name='register_customer'),
    
    
]

