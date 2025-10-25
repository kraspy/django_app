from random import randint

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

    @admin.action(description='Обнулить цены')
    def set_zero_prices(self, request, queryset: list[Product]):
        for product in queryset:
            product.price = 0
            product.save()

    @admin.action(description='Установить рандомные цены')
    def set_random_prices(self, request, queryset: list[Product]):
        for product in queryset:
            product.price = randint(100, 1000)
            product.save()

    @admin.action(description='Опубликовать')
    def set_published(self, request, queryset: list[Product]):
        for product in queryset:
            product.status = Product.Status.ACTIVE
            product.save()

    @admin.action(description='Снять с публикации')
    def set_unpublished(self, request, queryset: list[Product]):
        for product in queryset:
            product.status = Product.Status.INACTIVE
            product.save()

    actions = (
        set_zero_prices,
        set_random_prices,
        set_published,
        set_unpublished,
    )
