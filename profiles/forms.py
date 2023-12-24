from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].label = False


class UpdateUserForm(UserChangeForm):
    """
    A form for editing user information.

    """

    password = None

    class Meta:
        """Get User model, choose fields to display"""

        model = User
        fields = ["username", "first_name", "last_name"]
        help_texts = {"username": None}
