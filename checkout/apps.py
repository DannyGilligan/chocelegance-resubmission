from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        """
        When line item is saved or delted,
        this will trigger the updating of
        order totals automatically by calling
        the relevent model method.
        """
        import checkout.signals
