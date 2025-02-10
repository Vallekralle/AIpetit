from django import forms

from .ai import GeneriereRezept


class RecipeForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, max_length=213)

    def generate(self, input):
        return GeneriereRezept(input).response()
