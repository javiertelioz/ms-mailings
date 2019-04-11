from django.db import models
from django.utils import timezone
from django.contrib.sites.models import Site
from django.utils.translation import gettext_lazy as _

from ckeditor.fields import RichTextField

# Create your models here.
HTML_HELP_TXT = """
    Content of the header (html), variables or
    dynamic content {{myvar}} eg: {{name}}.
"""

class Brand(models.Model):

    name = models.CharField(max_length=150, unique=True, db_index=True)
    logo = models.ImageField(upload_to='brand_logo/%Y/%m/%d', blank=True)
    status = models.BooleanField(default=False)
    header_content = RichTextField(verbose_name=_('Header'), help_text=_(HTML_HELP_TXT))
    footer_content = RichTextField(verbose_name=_('Footer'), help_text=_(HTML_HELP_TXT))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def templates(self):
        return self.brand.all()

    class Meta:
        app_label = "mailings"
        ordering = ('name', )
        verbose_name = _('brand')
        verbose_name_plural = _('brand')
