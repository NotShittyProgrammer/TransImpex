
from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', main),
    path('about', about),
    path('blog', blog),
    path('portfolio-details/<int:name>', portfolio_details),
    path('services-details/<int:name>', services_details),
    path('blog-single/<int:name>', single_blog),
     path('blog-single/<int:name>/', single_blog, name='blog-single'),

]