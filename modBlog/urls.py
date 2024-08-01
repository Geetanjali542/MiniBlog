from django.urls import path
from . import views

urlpatterns = [
    path('add', views.add, name='add'),
    path('editblog/<int:pk>/', views.editblog, name='editblog'),
    path('deleteblog/<int:pk>/', views.deleteblog, name='deleteblog'),
    path('about', views.about, name="about"),
    path('contact', views.contact, name='contact'),
    path('privacypolicy', views.privacypolicy, name='privacypolicy'),
    path('termsconditions', views.termsconditions, name='termsconditions'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name="signup"),
    path('continueread', views.continueread, name="continueread"),


]




