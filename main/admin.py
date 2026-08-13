from django.contrib import admin
from .models import PortfolioItem, PhotographyCategory, PhotographyImage

# Register your models here.
@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'ecosystem', 'category', 'created_at')
    list_filter = ('ecosystem', 'category')
    search_fields = ('title', 'category')
    prepopulated_fields = {'slug': ('title',)} # Automatically creates a slug as you type the title

class PhotographyImageInline(admin.TabularInline):
    model = PhotographyImage
    extra = 5  # Pre-loads 5 image upload slots in admin
    fields = ('image', 'order')

@admin.register(PhotographyCategory)
class PhotographyCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'order')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [PhotographyImageInline]
    ordering = ('order', 'title')