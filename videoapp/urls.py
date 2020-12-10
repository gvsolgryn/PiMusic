from django.urls import path
from . import views

# Add URLConf
urlpatterns = [
    path('', views.v_main, name='v_main')
]
