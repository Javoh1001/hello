from django.urls import path
from . import views
# from django.db.models import auth_views


urlpatterns = [
    path('sign_in', views.sign_in, name='sign_in'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('logout', views.logout, name='logout')
]