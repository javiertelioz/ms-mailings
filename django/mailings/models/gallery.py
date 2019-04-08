from django.db import models
from django.utils import timezone
from django.contrib.sites.models import Site
from django.utils.translation import gettext_lazy as _

from .template import Template

# Create your models here.
class Gallery(models.Model):

    image = models.ImageField(upload_to='gallery/%Y/%m/%d', blank=True)
    template = models.ForeignKey(Template, related_name='gallery', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        app_label = "mailings"
        verbose_name = _("gallery")
        verbose_name_plural = _("gallery")
        ordering = ('id', )
