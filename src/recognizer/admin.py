from django.contrib import admin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from django.shortcuts import render
from django.urls import path
from django.utils.crypto import get_random_string
from django.utils.safestring import mark_safe
from recognizer.exceptions import TrainingErrorException
from recognizer.forms import PhotoToRecognizeAdminForm
from recognizer.models import Person
from recognizer.models import PersonDatabase
from recognizer.models import PersonPhoto


def make_thumb(instance):
    if instance.file.url is not None:
        return mark_safe(f'<img src={instance.file.url} height="120"/>')
    else:
        return ""


class PersonPhotoInline(admin.TabularInline):
    model = PersonPhoto
    fields = ["thumb", "file", "processed", "processed_error"]
    readonly_fields = ["thumb", "processed", "processed_error"]
    extra = 0
    can_delete = False

    def thumb(self, instance):
        return make_thumb(instance)


@admin.register(PersonDatabase)
class PersonDatabaseAdmin(admin.ModelAdmin):
    pass


@admin.action(description="Training person(s) photo(s)")
def training_images(modeladmin, request, queryset):
    persons_ids = queryset.values_list("id", flat=True)
    photos = PersonPhoto.objects.filter(
        person__id__in=persons_ids, processed=False, processed_error=False
    )
    counter = 0
    for photo in photos:
        if counter == 5:
            messages.add_message(request, messages.WARNING, "Only 5 photos per time")

        try:
            photo.training()
        except TrainingErrorException as training_error:
            messages.add_message(request, messages.WARNING, training_error)

        counter += 1


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name", "database", "photos", "trained"]
    inlines = [PersonPhotoInline]
    list_filter = ["database"]
    change_list_template = "admin/person_list.html"
    actions = [training_images]

    def trained(self, instance):
        if instance.photos.filter(processed=True).exists():
            return mark_safe('<img src="/static/admin/img/icon-yes.svg" alt="True">')

        return mark_safe('<img src="/static/admin/img/icon-no.svg" alt="False">')

    def photos(self, instance):
        return instance.photos.all().count()

    def recognize(self, request, extra_context=None):
        results = []
        submited_photo = None
        if request.method == "POST":
            form = PhotoToRecognizeAdminForm(request.POST, request.FILES)
            if form.is_valid():
                file = form.cleaned_data.get("photo")
                file_extension = file.name.split(".")[1]
                file_name = get_random_string(length=12)
                file_to_verify = f"check/{file_name}.{file_extension}"
                with default_storage.open(file_to_verify, "wb+") as destiny:
                    for chunk in file.chunks():
                        destiny.write(chunk)

                results = Person.sql_search_face(
                    image_file=file_to_verify, after_remove=False
                )
                submited_photo = file_to_verify

                if len(results) > 0:
                    messages.add_message(
                        request,
                        messages.SUCCESS,
                        f"There are {len(results)} similar faces found!",
                    )
                else:
                    messages.add_message(
                        request, messages.WARNING, "No similar face found"
                    )

        else:
            form = PhotoToRecognizeAdminForm()

        context = dict(
            self.admin_site.each_context(request),
            form=form,
            results=results,
            submited_photo=submited_photo,
        )

        return render(request, "admin/recognizer.html", context)

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [
            path(
                "recognize/",
                login_required(self.recognize),
                name="person_recognize",
            )
        ]
        return new_urls + urls


@admin.register(PersonPhoto)
class PersonPhotoAdmin(admin.ModelAdmin):
    search_fields = ["person__name"]
    list_display = ["uuid", "person", "thumb", "processed", "processed_error"]
    list_filter = ["processed", "processed_error"]
    raw_id_fields = ["person"]

    def thumb(self, instance):
        return make_thumb(instance)
