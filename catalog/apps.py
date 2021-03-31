from django.apps import AppConfig


class CatalogConfig(AppConfig):
    name = 'catalog'
    verbose_name = 'Catálogo'
    
    def ready(self):
        Product = self.get_model('Product')
