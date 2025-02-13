from django import forms

from .models import BulletPoint


class BulletPointForm(forms.ModelForm):
    class Meta:
        model = BulletPoint
        fields = ("text",)