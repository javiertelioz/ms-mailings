from django.db import models
from django.utils import timezone
from django.contrib.sites.models import Site
from django.utils.translation import gettext_lazy as _

from .brand import Brand
from .footer import Footer
from .header import Header

# Create your models here.
class Template(models.Model):

    brand = models.ForeignKey(Brand, related_name='brand', on_delete=models.CASCADE)
    name = models.CharField(max_length=150, unique=True, db_index=True)
    description = models.TextField(blank=True,)
    header = models.OneToOneField(Header, unique=True, related_name='header', on_delete=models.CASCADE)
    footer = models.OneToOneField(Footer,  unique=True, related_name='footer', on_delete=models.CASCADE)
    content = models.TextField(blank=True,)
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
