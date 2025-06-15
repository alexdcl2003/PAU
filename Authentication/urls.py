from django.urls import path
from Authentication.Views import views_login
from reconocimiento import views


urlpatterns = [
    path('', views_login.home_view, name='home'),
    path('signup/', views_login.signup_view, name='signup'),
    path('signin/', views_login.signin_view, name='signin'),
    path('logout/', views_login.logout_view, name='logout'),
    path('inicio/', views.dashboard, name='inicio'),
    path('reset/request/', views_login.request_reset_view, name='password_reset_custom'),
    path('reset/code/', views_login.verify_code_view, name='verify_code'),
    path('reset/new/', views_login.set_new_password_view, name='set_new_password'),
]