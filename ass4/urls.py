from django.urls import path, include


from django.urls import path
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter

from .views import register, setup_2fa, SecureDataViewSet

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('tasks/', include('tasks.urls')),
    path('setup-2fa/', setup_2fa, name='setup_2fa'),
]

router = DefaultRouter()
router.register('secure-data', SecureDataViewSet)

urlpatterns += router.urls