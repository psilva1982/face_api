from django.core.management.base import BaseCommand
from recognizer.exceptions import TrainingErrorException
from recognizer.models import PersonPhoto


class Command(BaseCommand):
    help = "Training person photos"

    def handle(self, *args, **kwargs):

        photos = PersonPhoto.objects.filter(
            processed=False, processed_error=False
        ).order_by("person__name")
        for photo in photos:

            try:
                photo.training()
                self.stdout.write(self.style.SUCCESS(f"{photo.file.name} trained!"))

            except TrainingErrorException as training_error:
                self.stdout.write(self.style.ERROR(training_error))
