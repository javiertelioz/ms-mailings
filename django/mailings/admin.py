from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

# Register your models here.
from .models import (
    Brand,
    Template,
    Mailings
)

class MailingsInline(admin.TabularInline):
    model = Mailings
    extra = 0

class BrandAdmin(admin.ModelAdmin):

    save_on_top = True
    list_per_page = 30

    list_display = ['name', 'image_tag', 'status', 'created_at', 'updated_at']
    list_filter = ['name', 'status', 'created_at', 'updated_at']
    inlines = [ MailingsInline ]


class TemplateAdmin(admin.ModelAdmin):

    save_on_top = True
    list_per_page = 30

    search_fields = ['name', 'subject', 'description']
    list_display = ['name', 'subject', 'description', 'status', 'brand']
    list_filter = ['name', 'status', 'created_at', 'updated_at']

admin.site.register(Brand, BrandAdmin)
admin.site.register(Template, TemplateAdmin)
