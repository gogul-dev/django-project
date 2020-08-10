from django.urls import path
from blog import views

urlpatterns = [
     path('home',views.Home.as_view(),name='home'),
     path('home/blogs/',views.Blogs.as_view(),name = 'blogs'),
]
