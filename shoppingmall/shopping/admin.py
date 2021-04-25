from shopping.models import Shopping
from django.contrib import admin 

# Register your models here.

class ShoppingAdmin(admin.ModelAdmin):
    list_display = ('name','brand','price')

admin.site.register(Shopping, ShoppingAdmin)