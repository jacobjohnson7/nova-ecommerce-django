
from django.contrib import admin
from django.contrib.auth.models import User
from .models import Category, Product, Banner

admin.site.site_header = "NOVA Studio Admin"
admin.site.site_title = "NOVA Admin Portal"
admin.site.index_title = "Storefront Management Dashboard"

original_each_context = admin.site.each_context

def custom_each_context(request):
    context = original_each_context(request)
    context["product_count"] = Product.objects.count()
    context["category_count"] = Category.objects.count()
    context["banner_count"] = Banner.objects.count()
    context["user_count"] = User.objects.count()
    return context

admin.site.each_context = custom_each_context


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "image_url", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "is_featured", "is_active")
    list_filter = ("category", "is_featured", "is_active")
    search_fields = ("name", "description")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ("title", "position", "is_active")
    list_filter = ("is_active",)
    search_fields = ("title",)
