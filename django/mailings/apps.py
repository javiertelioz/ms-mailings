from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class MailingsConfig(AppConfig):
    name = 'mailings'
    verbose_name = _('Mailings')
