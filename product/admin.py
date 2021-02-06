from .models import Category,Product,Images
from django.contrib import admin

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','status']
    list_filter = ['title']

class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 5           #dine suratlarun ucin dal islendik yagdayada hem gorkezilip bilinir

class ProductAdmin(admin.ModelAdmin):
    list_display = ['image_tag','title','category']
    readonly_fields = ('image_tag',)
    list_filter = ['title','category']
    inlines = [ProductImageInline]

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title','image_tag']
    readonly_fields = ('image_tag',)


admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)    
admin.site.register(Images,ImagesAdmin)