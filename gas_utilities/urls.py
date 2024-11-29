from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from service_requests import views as service_views
from service_requests import views


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True  


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.homepage, name='home'),
    path('requests/', include('service_requests.urls')),
     path('accounts/login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
]