from django.contrib import admin
from .models import Category, Product, Client, Sale
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname']


class ProductAdmin(admin.ModelAdmin):
    exclude = ['user']
    def has_change_permission(self, request, obj=None):
        return obj and obj.user == request.user

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(ProductAdmin, self).save_model(request, obj, form, change)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Client, ClientAdmin, )
admin.site.register(Product, ProductAdmin, )
admin.site.register(Sale)
