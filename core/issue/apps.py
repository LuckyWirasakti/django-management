from django.apps import AppConfig


class IssueConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.issue'
    
    def ready(self):
        import core.issue.signals
