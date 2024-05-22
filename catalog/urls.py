from django.urls import path
from . import views
from django.urls import re_path
from catalog import views as catalog_views
from .views import create_ad, edit_ad, delete_ad
from .views import ad_search



urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^$', views.index, name='index'),
    path('register/', catalog_views.register, name='register'),
    path('profile/', catalog_views.profile, name='profile'),

    path('create/', create_ad, name='create_ad'),
    path('edit/<int:ad_id>/', edit_ad, name='edit_ad'),
    path('delete/<int:ad_id>/', delete_ad, name='delete_ad'),
    path('ad_search/', ad_search, name='ad_search'),


]


