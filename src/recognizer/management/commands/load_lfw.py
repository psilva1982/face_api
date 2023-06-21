from django.conf import settings
from django.core.files import File
from django.core.management.base import BaseCommand
from recognizer.models import Person
from recognizer.models import PersonDatabase
from recognizer.models import PersonPhoto
from urllib import request
import os
import shutil
import tarfile


class Command(BaseCommand):
    help = "Download and load LFW dataset into database"

    def handle(self, *args, **kwargs):

        self.stdout.write(self.style.WARNING("Download LFW dataset from internet..."))
        remote_url = 'https://vis-www.cs.umass.edu/lfw/lfw.tgz'
        dataset_file_path = f"{settings.BASE_DIR}/dataset/lfw.tgz"
        request.urlretrieve(remote_url, dataset_file_path)

        self.stdout.write(self.style.WARNING("Extracting LFW dataset..."))
        tgz_file = tarfile.open(dataset_file_path)
        tgz_file.extractall(f"{settings.BASE_DIR}/tmp/")
        tgz_file.close()

        self.stdout.write(
            self.style.WARNING("Loading LFW persons into database, please wait...")
        )
        folder = f"{settings.BASE_DIR}/tmp/lfw"
        database, created = PersonDatabase.objects.get_or_create(name="LFW")

        persons = [
            name
            for name in os.listdir(folder)
            if os.path.isdir(os.path.join(folder, name))
        ]
        for person in persons:
            person_name = person.replace("_", " ")
            new_person = Person.objects.create(name=person_name, database=database)

            origin_person_folder = f"{folder}/{person}"
            for file in os.listdir(origin_person_folder):
                if os.path.isfile(os.path.join(origin_person_folder, file)):
                    PersonPhoto.objects.create(
                        person=new_person,
                        file=File(
                            file=open(f"{origin_person_folder}/{file}", "rb"),
                            name=f"{file}",
                        ),
                    )

        self.stdout.write(self.style.SUCCESS("Load of people completed successfully!"))
        shutil.rmtree(folder)
