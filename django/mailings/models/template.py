from django.db import models
from django.utils import timezone
from django.contrib.sites.models import Site
from django.utils.translation import gettext_lazy as _

from ckeditor_uploader.fields import RichTextUploadingField

from .brand import Brand

HTML_HELP_TXT = """
    Content of the body (html), variables or
    dynamic content {{myvar}} eg: {{name}}.
"""
# Create your models here.
class Template(models.Model):

    name = models.CharField(verbose_name=_('name'), max_length=150, unique=True, db_index=True)
    description = models.CharField(verbose_name=_('description'), max_length=255, db_index=True)
    subject = models.CharField(verbose_name=_('subject'), max_length=255, db_index=True)
    content = RichTextUploadingField(verbose_name=_('content'), help_text=_(HTML_HELP_TXT))
    brand = models.ForeignKey(Brand, related_name='brand', on_delete=models.CASCADE)
    email_from = models.EmailField(verbose_name=_('email from'), help_text=_('ej. soport@mybrand.com'))
    status = models.BooleanField(verbose_name=_('status'), default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = "mailings"
        ordering = ('name', )
        verbose_name = _('template')
        verbose_name_plural = _('templates')
