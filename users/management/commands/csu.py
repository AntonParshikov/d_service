from django.core.management import BaseCommand

from users.models import Users


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = Users.objects.create(
            email='admin@pc.ru',
            first_name='Admin',
            last_name='Ad',
            is_superuser=True,
            is_staff=True,
            is_active=True

        )

        user.set_password('324214Kross!')
        user.save()
