from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'

    def ready(self) :
        import user.signals
        return super().ready()
