from recognizer.api.serializers.recognizer import RecognizerResult
from recognizer.api.serializers.recognizer import UploadPhotoSerializer
from recognizer.models import Person
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication


class RecognizerViewSet(viewsets.ViewSet):

    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = UploadPhotoSerializer

    def create(self, request):
        photo = request.FILES.get("photo", None)
        serializer = UploadPhotoSerializer(data={"photo": photo})
        serializer.is_valid(raise_exception=True)
        results = Person.sql_search_face(
            image_file=photo, in_memory_file=True, after_remove=False
        )

        if len(results) > 0:
            serializer_results = RecognizerResult(
                results, context={"request": request}, many=True
            )
            return Response(
                {"result": serializer_results.data}, status=status.HTTP_200_OK
            )
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class FaceRecognitionApiCheck(viewsets.ViewSet):
    def list(self, request):
        data = {"status": "OK", "service": "Face recognition api"}
        return Response(data=data, status=status.HTTP_200_OK)
