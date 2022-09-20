from django.urls import path
from my_app import views

urlpatterns = [
    path('', views.get_home_page, name = 'home'),
    path('about/', views.get_about_page, name = 'about'),
    path('signup/', views.signup, name = 'signup'),
    path('sides/', views.sides, name = 'sides'),


]