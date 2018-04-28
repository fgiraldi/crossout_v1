from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
# development mode, static files
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
   path('', views.welcome, name='index'),
   path('login/', auth_views.LoginView.as_view(template_name='game/login.html'), name='login'),
   path('users/storage/', views.user_storage, name='user_storage'),
   path('users/garage/', views.garage, name='garage'),
   path('users/market/', views.market, name='market'),
   path('users/factions/', views.factions, name='factions'),
   path('users/logout/', views.logout_view, name='logout'),
   path('users/loggedout/', views.loggedout, name='loggedout'),
   path('config/', views.config_menu, name='config_menu'),
   path('config/raritys/', views.config_raritys, name='config_raritys'),
]