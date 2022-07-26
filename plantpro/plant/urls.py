from django.urls import path

from plant import views

urlpatterns = [

  path('redirect', views.take_img, name='take_img'),
  path('',views.home,name='home'),
    ]