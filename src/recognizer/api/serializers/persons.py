from recognizer.models import Person
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):

    avatar = serializers.SerializerMethodField()
    database = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Person
        fields = [
            "uuid",
            "avatar",
            "name",
            "database",
        ]

    def get_avatar(self, person):
        request = self.context.get("request")
        avatar = person.photos.first()
        return request.build_absolute_uri(avatar.file.url)


class PersonWithPhotosSerializer(PersonSerializer):
    photos = serializers.SerializerMethodField()

    class Meta(PersonSerializer.Meta):
        fields = PersonSerializer.Meta.fields + ["photos"]

    def get_photos(self, person):
        request = self.context.get("request")
        return [
            {
                "processed": photo.processed,
                "url": request.build_absolute_uri(photo.file.url),
            }
            for photo in person.photos.all()
        ]
