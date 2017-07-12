from django.core.management.base import BaseCommand, CommandError
from import_data import import_reviews_data


class Command(BaseCommand):
    help = 'Imports the data from reviews.csv and store it in the database'
   
    def handle(self, *args, **options):
        try:
            import_reviews_data()
        except:
            raise CommandError('Error importing data')
