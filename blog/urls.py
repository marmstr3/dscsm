from django.urls import path

from . import views

urlpatterns = [path('', views.home_page, name='home_page'),
               path('blog', views.post_list, name='blog'),
               path('blog/<int:pk>', views.post_detail, name='post_detail'),
               ]