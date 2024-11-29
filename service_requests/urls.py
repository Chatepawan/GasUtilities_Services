from django.urls import path
from . import views


app_name = 'service_requests'

urlpatterns = [
    path('new/', views.create_service_request, name='create_service_request'),
    path('list/', views.list_service_requests, name='list_service_requests'),
    path('new/', views.create_service_request, name='create_request'),
    path('track/', views.track_requests, name='track_requests'),  # View all requests
    path('track/<int:pk>/', views.request_details, name='request_details'),  # View specific request details
    path('update/<int:pk>/', views.update_request_status, name='update_request_status'),
    path('account/', views.account_info, name='account_info'),
    path('dashboard/', views.representative_dashboard, name='representative_dashboard'),
    path('', views.homepage, name='home'),
]
