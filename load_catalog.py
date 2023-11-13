# api/management/commands/load_catalog.py
from django.core.management.base import BaseCommand
from api.models import load_catalog_from_excel

class Command(BaseCommand):
    help = 'Load the product catalog from Excel file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the Excel file')

    def handle(self, *args, **options):
        file_path = options['file_path']
        load_catalog_from_excel(file_path)
        self.stdout.write(self.style.SUCCESS('Successfully loaded the product catalog'))
