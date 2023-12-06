from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', RedirectView.as_view(url='login/')),  # Redirect root URL to the login page
    path('', include('bakery.urls')),  # Include bakery app's URLs
    # path('login/', auth_views.LoginView.as_view(template_name='bakery_home.html'), name='login'),  # Login URL
]

