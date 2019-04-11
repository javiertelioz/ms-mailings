from django.db import models
from django.utils import timezone
from django.contrib.sites.models import Site
from django.utils.translation import gettext_lazy as _

from .brand import Brand

# Create your models here.
class Mailings(models.Model):

    brand = models.ForeignKey(Brand, verbose_name=_('Brand'), related_name='emails_brand', on_delete=models.CASCADE)
    name = models.CharField(verbose_name=_('Sender Name'), max_length=150, unique=True, db_index=True)
    email = models.EmailField(verbose_name=_('Email'), help_text=_('eg. soport@mybrand.com'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    def __str__(self):
        return "%s - %s" % (self.name, self.email)

    class Meta:
        app_label = "mailings"
        verbose_name = _("Mailing")
        verbose_name_plural = _("Mailings")
        ordering = ('id', )
