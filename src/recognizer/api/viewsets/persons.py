from django_filters.rest_framework import DjangoFilterBackend
from recognizer.api.serializers.persons import PersonWithPhotosSerializer
from recognizer.models import Person
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.filters import OrderingFilter
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class PersonListDetailViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):

    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = PersonWithPhotosSerializer
    queryset = Person.objects.all()
    lookup_field = "uuid"

    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    search_fields = ["name"]
    filterset_fields = ["database"]
