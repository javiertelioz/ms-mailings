import json
import uuid

from django.db import models
from django.utils import timezone
from django.contrib.sites.models import Site
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers.data import JsonLexer

from .template import Template

# Create your models here.
class Mail(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    template = models.ForeignKey(Template, verbose_name=_('Template'), on_delete=models.CASCADE)
    params = models.TextField(verbose_name=_('Request Params'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    def __str__(self):
        return str(self.id)

    class Meta:
        app_label = "mailings"
        verbose_name = _("Postal System")
        verbose_name_plural = _("Postal System")
        ordering = ('id', )

    def detail_json_formatted(self):

        # with JSON field, no need to do .loads
        data = json.dumps(json.loads(self.params), indent=2)

        # format it with pygments and highlight it
        formatter = HtmlFormatter(style='colorful')
        response = highlight(data, JsonLexer(), formatter)

         # include the style sheet
        #style = "<style>" + formatter.get_style_defs() + "</style><br/>"
        #return mark_safe(style + response)
        return mark_safe('<textarea rows="15" cols="120">%s</textarea>' % data)

    detail_json_formatted.short_description = 'Details Formatted'
    detail_json_formatted.allow_tags = True
