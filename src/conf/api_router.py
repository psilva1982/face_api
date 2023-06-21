from recognizer.api.viewsets.persons import PersonListDetailViewSet
from recognizer.api.viewsets.recognizer import FaceRecognitionApiCheck
from recognizer.api.viewsets.recognizer import RecognizerViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("persons", PersonListDetailViewSet, "persons")
router.register("facial-recognition", RecognizerViewSet, "recognition")
router.register("check-me", FaceRecognitionApiCheck, "check-me")

urlpatterns = router.urls
