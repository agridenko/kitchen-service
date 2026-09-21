from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from kitchen.models import DishType


class DishTypeForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = "__all__"