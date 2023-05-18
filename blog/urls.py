from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import product_view, images_by_product_name



urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('shop/', views.shop, name='shop'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('product/', product_view, name='product'),
    path('images/', images_by_product_name, name='images_by_product_name'),
] + static(settings.MEDIA_URL, documents_root=settings.MEDIA_ROOT)