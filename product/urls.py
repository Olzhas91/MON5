from django.urls import path

from product import views


urlpatterns = [
    path('products/categories/', views.category_list_api_view),
    path('products/categories/<int:id>/', views.category_detail_api_view),
    path('products/products/', views.product_list_api_view),
    path('products/products/<int:id>/', views.product_detail_api_view),
    path('products/reviews/', views.review_list_api_view),
    path('products/reviews/<int:id>/', views.review_detail_api_view),
    path('productss', views.product_review_list_api_view)
]