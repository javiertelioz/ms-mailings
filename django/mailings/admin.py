from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

# Register your models here.
from .models import (
    Brand,
    Template,
    Gallery
)

class BrandAdmin(admin.ModelAdmin):

    save_on_top = True
    list_per_page = 30

    list_display = ['name', 'status', 'created_at', 'updated_at']
    list_filter = ['name', 'status', 'created_at', 'updated_at']

class GalleryInline(admin.TabularInline):
    model = Gallery
    extra = 0

class TemplateAdmin(admin.ModelAdmin):

    save_on_top = True
    list_per_page = 30

    list_display = ['name', 'description', 'status', 'created_at', 'updated_at']
    list_filter = ['name', 'status', 'created_at', 'updated_at']
    inlines = [ GalleryInline ]

admin.site.register(Brand, BrandAdmin)
admin.site.register(Template, TemplateAdmin)
