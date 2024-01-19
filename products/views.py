from django.db.models import Count, Avg, ExpressionWrapper, F, fields
from rest_framework import viewsets, filters, pagination
from .models import Product, Review, WishList
from .serializers import *



class CustomPageNumberPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['price', 'popularity']
    search_fields = ['name', 'description', 'category__name']
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        queryset = Product.objects.annotate(
            popularity=ExpressionWrapper(
                (Count('purchase', distinct=True, output_field=fields.IntegerField()) + Avg('review__rating')) / 2,
                output_field=fields.DecimalField(max_digits=10, decimal_places=2)
            )
        ).distinct()

        return queryset

class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created', 'rating']

class WishListViewset(viewsets.ModelViewSet):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['list_name', 'items']
    pagination_class = CustomPageNumberPagination
    
class PurchaseViewset(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['purchase_date']
    serializer_class = PurchaseSerializer
   
