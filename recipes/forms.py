from django import forms

from .models import Recipe
from .ai import GeneriereRezept


class RecipeForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea)

    def generate(self, input):
        return GeneriereRezept(input).response()
    
    class Meta:
        model = Recipe
        fields = ("text",)
