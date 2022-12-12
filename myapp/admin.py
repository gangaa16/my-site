from myapp.models import Cart, Product
from django.contrib import admin

# Register your models here.
admin.site.register(Product)
@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']