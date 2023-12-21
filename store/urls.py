from django.urls import path
from .import views

urlpatterns =[
    path('',views.store,name='store'),
    path('<slug:category_slug>/',views.store,name='products_by_category'),
    path('<slug:category_slug>/<product_slug>/',views.product_detail,name='products_detail'),
    # path('<slug:category_slug>/',views.products_by_category,name='product_category'),
]