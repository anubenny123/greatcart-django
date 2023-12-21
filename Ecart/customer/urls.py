from django.urls import path
from customer import views
urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('products/<int:pk>',views.ProductDetailsView.as_view(),name='product-detail'),
    path('addcart/<int:id>',views.AddToCartView.as_view(),name='addcart'),
    path('cart/all/',views.CartListView.as_view(),name='cart-list'),
    path("products/<int:pk>/delete",views.CartRemoveView.as_view(),name="cart-remove"),
]
