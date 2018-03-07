from django.urls import path
from django.contrib.auth import auth
from . import views
# development mode, static files
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
   path('', views.welcome, name='index'),
   path('login/', auth_views.LoginView.as_view(template_name='game/login.html'), name='login'),
   path('users/<int:user_id>/storage/', views.user_storage, name='user_storage'),
]