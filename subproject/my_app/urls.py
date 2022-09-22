from django.urls import path
from my_app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.get_home_page, name = 'home'),
    path('about/', views.get_about_page, name = 'about'),
    path('createpost/', views.createpost, name= 'createpost'),
    path('signup/', views.signup, name = 'signup'),
    path('sides/', views.sides, name = 'sides'),
    path('signin/',auth_views.LoginView.as_view(template_name='my_app/signin.html'), name='signin'),
    path('signout/',auth_views.LogoutView.as_view(template_name='my_app/signout.html'), name='signout')

]