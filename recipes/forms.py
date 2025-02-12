from django import forms

from .models import Recipe
from .ai import GeneriereRezept


class RecipeForm(forms.ModelForm):
    text = forms.CharField(
        widget=forms.Textarea, 
        label="Informationen",
        help_text="z.B. Ein frisches russisches Gericht mit Paprika, Möhre, Reis und Fleisch",
        max_length=191,
        )

    def generate(self, input):
        return GeneriereRezept(input).response()
    
    class Meta:
        model = Recipe
        fields = ("text",)
