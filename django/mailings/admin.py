from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

# Register your models here.
from .models import (
    Brand,
    Template,
    Mailings,
    Mail,
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

class MailAdmin(admin.ModelAdmin):

    save_on_top = False
    list_per_page = 30

    search_fields = ['id', 'to', 'template__name']
    list_display = ['id', 'to', 'template', 'status', 'created_at' ]
    list_filter = ['template', 'status', 'created_at', 'updated_at']

    fieldsets = [
        (_("General"), {
            'fields': [
                ('to', 'status'),
                ('template', 'created_at'),
            ]
        }),
        (_("Request Params"), {
            'fields': ['detail_json_formatted']
        }),
    ]

    readonly_fields = ('to', 'status', 'template',  'created_at', 'detail_json_formatted',)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Brand, BrandAdmin)
admin.site.register(Template, TemplateAdmin)
admin.site.register(Mail, MailAdmin)
