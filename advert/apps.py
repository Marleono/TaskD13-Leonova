from django.apps import AppConfig


class AdvertConfig(AppConfig):
    name = 'advert'

    def ready(self):
        import advert.signals
