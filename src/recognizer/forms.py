from django import forms
from django.core.validators import FileExtensionValidator


class PhotoToRecognizeAdminForm(forms.Form):
    photo = forms.ImageField(
        validators=[FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png"])],
        help_text="O arquivo necessita ser do tipo JPG ou PNG.",
    )
