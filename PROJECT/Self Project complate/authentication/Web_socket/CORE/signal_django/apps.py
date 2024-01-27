from django.apps import AppConfig


class SignalDjangoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'signal_django'


    def ready(self):
        import signal_django. signals

