from django.urls import path
from Api import views
from rest_framework import routers
from rest_framework.routers import DefaultRouter

router = routers.DefaultRouter()
router.register("categories",views.CategoryViewSetView,basename='categories'),
router.register("products",views.ProductViewSetView,basename='products')

urlpatterns = [


]+router.urls
