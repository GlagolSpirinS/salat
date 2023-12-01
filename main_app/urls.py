from django.contrib import admin
from django.urls import path, include
import main_app.views
from main_app import views

urlpatterns = [
    path('', views.index, name="main"),
    path('about/', views.about, name="about"),
    path('blog-home/', views.blog_home, name='blog_home'),
    path('blog-post/', views.blog_post, name='blog_post'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('portfolio-item/', views.portfolio_item, name='portfolio_item'),
    path('portfolio-overview/', views.portfolio_overview, name='portfolio_overview'),
    path('pricing/', views.pricing, name='pricing'),
    path('base/', views.base, name='base'),
    path('catalog/', views.catalog, name='catalog'),
    path('product/<int:product_id>/', views.product, name='product'),
]
