from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Product)
admin.site.register(Review)
class WishListAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('list_name',)}
    list_display = ['list_name', 'slug']
    
admin.site.register(WishList, WishListAdmin)