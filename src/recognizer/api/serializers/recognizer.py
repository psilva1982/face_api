from recognizer.api.serializers.persons import PersonSerializer
from rest_framework import serializers


class UploadPhotoSerializer(serializers.Serializer):
    photo = serializers.ImageField(required=True)


class RecognizerResult(serializers.Serializer):
    accuracy = serializers.CharField(max_length=10)
    person = PersonSerializer()
