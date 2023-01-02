from django.contrib import admin

# Register your models here.

from .models import Product, ReviewRating, ProductGallery,Category, Variation,Banner, BannerProduct

class VariationInline(admin.TabularInline):
    model = Variation
    extra = 1

class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'our_price', 'stock', 'category', 'is_available', 'created_date', 'modified_date')
    prepopulated_fields = {'slug': ('product_name',)}
    inlines = [VariationInline, ProductGalleryInline]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'slug')
    prepopulated_fields = {'slug': ('category_name',)}

class BannerProductInline(admin.TabularInline):
    model = BannerProduct
    extra = 1

class BannerAdmin(admin.ModelAdmin):
    inlines = [BannerProductInline]
    prepopulated_fields = {'slug': ('name',)}
    # list_display = ('name', ')

admin.site.register(Product, ProductAdmin)
admin.site.register(ReviewRating)
admin.site.register(ProductGallery)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Variation)
admin.site.register(Banner, BannerAdmin)
# admin.site.register(VariationManager)
