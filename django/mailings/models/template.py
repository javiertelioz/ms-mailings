from django.db import models
from django.utils import timezone
from django.contrib.sites.models import Site
from django.utils.translation import gettext_lazy as _

from ckeditor.fields import RichTextField

from .brand import Brand

HTML_HELP_TXT = """
    Content of the body (html), variables or
    dynamic content {{myvar}} eg: {{name}}.
"""
# Create your models here.
class Template(models.Model):

    name = models.CharField(max_length=150, unique=True, db_index=True)
    description = models.CharField(max_length=255, db_index=True)
    content = RichTextField(verbose_name=_('Content'), help_text=_(HTML_HELP_TXT))
    brand = models.ForeignKey(Brand, related_name='brand', on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = "mailings"
        ordering = ('name', )
        verbose_name = _('template')
        verbose_name_plural = _('templates')
