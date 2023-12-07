
from django.contrib import admin
from django.urls import path, include
from main_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
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

    # URL-маршруты для продуктов (Product)
    path('product/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', views.ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),

    # URL-маршруты для категорий (Category)
    path('category/', views.CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('category/create/', views.CategoryCreateView.as_view(), name='category_create'),

    # URL-маршруты для тегов (Tag)
    path('tag/', views.TagListView.as_view(), name='tag_list'),
    path('tag/<int:pk>/', views.TagDetailView.as_view(), name='tag_detail'),
    path('tag/create/', views.TagCreateView.as_view(), name='tag_create'),
    path('tag/<int:pk>/update/', views.TagUpdateView.as_view(), name='tag_update'),
    path('tag/<int:pk>/delete/', views.TagDeleteView.as_view(), name='tag_delete'),

    # URL-маршруты для заказов (Order)
    path('order/', views.OrderListView.as_view(), name='order_list'),
    path('order/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('order/create/', views.OrderCreateView.as_view(), name='order_create'),
    path('order/<int:pk>/update/', views.OrderUpdateView.as_view(), name='order_update'),
    path('order/<int:pk>/delete/', views.OrderDeleteView.as_view(), name='order_delete'),

]
