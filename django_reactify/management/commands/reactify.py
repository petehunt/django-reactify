from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
import subprocess

class Command(BaseCommand):
    help = 'Run reactify and build your React app'

    def handle(self, *args, **options):
        try:
            flags = ''
            if settings.DEBUG:
                flags = ' -w -d'

            subprocess.check_call(
                'reactify%s -o %r -b %r %s' % (
                    flags,
                    settings.REACTIFY_BUNDLE_PATH,
                    settings.REACTIFY_SRC,
                    ' '.join(repr(module_id) for module in settings.REACTIFY_MODULE_IDS)
                ),
                shell=True
            )
        except e:
            raise CommandError(
                'There was an error running reactify. Be sure it is installed and all settings are configured. The error was: ' + str(e)
            )
