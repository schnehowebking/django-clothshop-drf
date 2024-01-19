from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter()

router.register('list', views.ProductViewset) 
router.register('reviews', views.ReviewViewset)
router.register('wishlist', views.WishListViewset)
router.register('purchase', views.PurchaseViewset)
urlpatterns = [
    path('', include(router.urls)),
    
]