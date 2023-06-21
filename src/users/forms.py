from crispy_forms.helper import FormHelper
from crispy_forms.layout import Button
from crispy_forms.layout import Column
from crispy_forms.layout import Div
from crispy_forms.layout import Layout
from crispy_forms.layout import Row
from crispy_forms.layout import Submit
from django import forms
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

User = get_user_model()


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["name", "avatar"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "user-detail-form"
        self.helper.attrs = {"novalidate": ""}
        self.helper.layout = Layout(
            Div(
                Row(
                    Column("name", css_class="form-group col-md-12 mb-0"),
                    css_class="form-row",
                ),
                Row(
                    Column("avatar", css_class="form-group col-md-12 mb-0"),
                    css_class="form-row",
                ),
                css_class="card-body",
            ),
            Div(
                Button(
                    "change-password",
                    "Change password",
                    css_class="btn btn-danger",
                    onClick=f"window.location='{ reverse_lazy('account_change_password')} '",
                ),
                Submit(
                    "submit",
                    "Save",
                ),
                css_class="card-footer d-flex justify-content-between",
            ),
        )


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["name", "email", "is_active", "is_staff", "is_superuser"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.attrs = {"novalidate": ""}
        self.helper.layout = Layout(
            Div(
                Row(
                    Column("email", css_class="form-group col-md-12 mb-0"),
                    css_class="form-row",
                ),
                Row(
                    Column("name", css_class="form-group col-md-12 mb-0"),
                    css_class="form-row",
                ),
                Row(
                    Column("is_active", css_class="form-group col-md-12 mb-0"),
                    css_class="form-row",
                ),
                Row(
                    Column("is_staff", css_class="form-group col-md-12 mb-0"),
                    css_class="form-row",
                ),
                Row(
                    Column("is_superuser", css_class="form-group col-md-12 mb-0"),
                    css_class="form-row",
                ),
                css_class="card-body",
            ),
            Div(
                Submit(
                    "submit",
                    "Save",
                ),
                css_class="card-footer d-flex justify-content-between",
            ),
        )
