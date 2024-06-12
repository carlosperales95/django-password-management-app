from django import forms
from .models import credential

# Reordering Form and View


class PositionForm(forms.Form):
    position = forms.CharField()


class CredentialForm(forms.ModelForm):
    class Meta:
        # specify model to be used
        model = credential

        # specify fields to be used
        fields = [
            "title",
            "username",
            "password",
            "last_updated",
            "owned"]
