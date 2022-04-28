from random import randrange

from django.core.management import BaseCommand

from apps.products.models import Product


class Command(BaseCommand):
    help = 'Populate available products db table'

    def handle(self, *args, **options):
        products = ['orange', 'banana', 'mango', 'grape', 'strawberry']

        Product.objects.bulk_create(
            Product(name=name, stock_quantity=randrange(100), price=randrange(100)**2/4) for name in products
        )

        self.stdout.write(self.style.SUCCESS('Successfully created new products'))
