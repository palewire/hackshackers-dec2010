from django.core.management.base import BaseCommand, CommandError
from unemployment import load

class Command(BaseCommand):
    help = 'Loads data for California unemployment'

    def handle(self, *args, **options):
        print 'Loading data for California unemployment'
        load.monthlys()
        print 'Successfully loaded data for California unemployment'
