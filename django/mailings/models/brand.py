from django.db import models
from django.utils import timezone
from django.contrib.sites.models import Site
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Brand(models.Model):

    name = models.CharField(max_length=150, unique=True, db_index=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = "mailings"
        ordering = ('name', )
        verbose_name = _('brand')
        verbose_name_plural = _('brand')
