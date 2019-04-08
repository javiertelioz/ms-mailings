from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Header(models.Model):

    name = models.CharField(max_length=150, unique=True, db_index=True)
    html_content = models.CharField(max_length=150, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = "mailings"
        ordering = ('id', )
        verbose_name = _('header')
        verbose_name_plural = _('headers')
