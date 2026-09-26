from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from kitchen.models import DishType, Dish, Cook


class DishTypeForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = "__all__"


class DishForm(forms.ModelForm):
    cooks = forms.ModelMultipleChoiceField(
        queryset=Cook.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Dish
        fields = "__all__"


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "years_of_experience",
            "first_name",
            "last_name",
        )


class DishTypeSearchForm(forms.Form):
    name = forms.CharField(
        required=False,
        label="",
        max_length=255,
        widget=forms.TextInput(
            attrs={"placeholder": "Search by name"}
        ),
    )


class DishSearchForm(forms.Form):
    name = forms.CharField(
        required=False,
        label="",
        max_length=255,
        widget=forms.TextInput(
            attrs={"placeholder": "Search by name"}
        ),
    )


class CookSearchForm(forms.Form):
    username = forms.CharField(
        required=False,
        label="",
        max_length=255,
        widget=forms.TextInput(
            attrs={"placeholder": "Search by username"}
        ),
    )
