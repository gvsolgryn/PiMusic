from django.urls import path
from . import views

# Add URLConf
urlpatterns = [
    path('login/', views.login_request, name='login'),
    path('signup/', views.signup_request, name='signup'),
    path('logout/', views.logout_request, name='logout'),
    path('v_login/', views.v_login_request, name='v_login'),
    path('v_signup/', views.v_signup_request, name='v_signup'),
    path('v_logout/', views.v_logout_request, name='v_logout'),
]
