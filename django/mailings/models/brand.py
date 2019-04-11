from django.db import models
from django.utils import timezone
from django.utils.html import format_html
from django.contrib.sites.models import Site
from django.utils.translation import gettext_lazy as _

from ckeditor.fields import RichTextField

# Create your models here.
HTML_HELP_TXT = """
    Content of the header (html), variables or
    dynamic content {{myvar}} eg: {{name}}.
"""

class Brand(models.Model):

    name = models.CharField(verbose_name=_('Name'), max_length=150, unique=True, db_index=True)
    logo = models.ImageField(verbose_name=_('Logo'), upload_to='brand_logo/%Y/%m/%d', blank=True)
    status = models.BooleanField(verbose_name=_('Status'), default=False)
    header_content = RichTextField(verbose_name=_('Header'), help_text=_(HTML_HELP_TXT))
    footer_content = RichTextField(verbose_name=_('Footer'), help_text=_(HTML_HELP_TXT))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    def __str__(self):
        return self.name

    @property
    def templates(self):
        return self.brand.all()

    class Meta:
        app_label = "mailings"
        ordering = ('name', )
        verbose_name = _('Brand')
        verbose_name_plural = _('Brands')

    def image_tag(self):
        if not self.logo:
            return

        return format_html(
            '<img src="{}" alt="{}" width="150" height="80" styles="width: 100%;height: auto;" />',
            self.logo.url,
            self.name,
        )

    image_tag.short_description = _('Logo')
    image_tag.allow_tags = True
