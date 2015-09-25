from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class PollsAppConfig(AppConfig):
    name = 'Polls'
    verbose_name = _('Polls')