from django.apps import AppConfig


class TeammateFinderAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'teammate_finder_app'

    def ready(self):
        import teammate_finder_app.signals