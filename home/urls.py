from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.index, name='index'),
    path('contact', views.contact_form, name='contact'),
    path('login', views.login_form),
    path('join', views.join_form),
    path('logout', views.login_out),

]