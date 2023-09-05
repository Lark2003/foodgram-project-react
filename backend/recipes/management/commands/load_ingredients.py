import csv

from django.core.management.base import BaseCommand
from recipes.models import Ingredient


class Command(BaseCommand):
    help = 'Загружает данные об ингридиентах в БД'

    def add_arguments(self, parser):
        parser.add_argument(
            'path_to_ingredients',
            type=str,
            help='По умолчанию ./data/ingredients.csv'
        )

    def handle(self, *args, **options):
        file_path = options['path_to_ingredients']
        self.stdout.write('Загрузка %s ...' % file_path)
        with open(file_path, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                ingredient, _ = Ingredient.objects.update_or_create(
                    name=row[0],
                    measurement_unit=row[1]
                )
        self.stdout.write(self.style.SUCCESS('Ингридиенты загружены'))
