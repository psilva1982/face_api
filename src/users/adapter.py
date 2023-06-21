from allauth.account.adapter import DefaultAccountAdapter
from django.utils.crypto import get_random_string


class UserAdapter(DefaultAccountAdapter):
    def generate_emailconfirmation_key(self, email):
        from allauth.account.models import EmailConfirmation

        while True:
            key = get_random_string(6).lower()
            exists = EmailConfirmation.objects.filter(key=key).exists()
            if not exists:
                break
        return key

    def save_user(self, request, user, form, commit=True):
        user.is_staff = True
        user.is_superuser = True
        return super().save_user(request, user, form, commit=True)
