from django.contrib import admin

from store.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    empty_value_display = '---'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ordering = ('pk',)
    list_filter = ('status',)
    list_display = ('name', 'slug', 'category', 'price', 'status')
    list_editable = ('slug', 'price')
    search_fields = ('name',)
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')
    raw_id_fields = ('category',)
    save_as = False
