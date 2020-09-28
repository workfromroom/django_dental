from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('about/', views.about, name="about"),
    path('blog/', views.blog, name="blog"),
    path('blog_details/', views.blog_details, name="blog_details"),
    path('contact/', views.contact, name="contact"),
    path('pricing/', views.pricing, name="pricing"),
    path('service/', views.service, name="service"),
]
