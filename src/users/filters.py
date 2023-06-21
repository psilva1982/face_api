from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div
from crispy_forms.layout import Layout
from crispy_forms.layout import Submit
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.forms.widgets import TextInput

import django_filters

User = get_user_model()


class UserFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(
        method="search_user",
        label="",
        widget=TextInput(attrs={"placeholder": "Search"}),
    )

    class Meta:
        model = User
        fields = ["search"]

    def search_user(self, queryset, field_name, value):
        if value != "":
            return queryset.filter(Q(email__icontains=value) | Q(name__icontains=value))
        return queryset

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "GET"
        self.helper.form_class = "form-inline"
        self.helper.attrs = {"novalidate": ""}
        self.helper.layout = Layout(
            Div(
                "search",
                Submit("submit", "Search", css_class="btn-default"),
                css_class="row",
            )
        )
