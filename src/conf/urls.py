from allauth.account.views import ConfirmEmailView
from allauth.account.views import email_verification_sent
from conf.api_router import router
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.urls import re_path
from django.views.generic import RedirectView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Facial recognition api",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path(
        "admin/login/", RedirectView.as_view(url="/accounts/login/"), name="admin:login"
    ),
    path("admin/", admin.site.urls),
    path("auth/", include("rest_framework.urls")),
    path("api/", include(router.urls)),
    path(
        "doc/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    re_path(
        r"^dj-rest-auth/registration/account-confirm-email/(?P<key>[-:\w]+)/$",
        ConfirmEmailView.as_view(),
        name="account_confirm_email",
    ),
    path(
        "dj-rest-auth/registration/account-email-verification-sent/",
        email_verification_sent,
        name="account_email_verification_sent",
    ),
    path("accounts/", include("allauth.urls")),
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
    path("dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")),
    path("", RedirectView.as_view(url="/admin"), name="to_admin"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Facial Recognition"
