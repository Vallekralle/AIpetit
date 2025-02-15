from django import forms

from .models import Recipe
from .ai import GeneriereRezept


class RecipeForm(forms.ModelForm):
    text = forms.CharField(
        widget=forms.Textarea(attrs={"maxlength": 191,}), 
        label="Informationen (maximal 191 Zeichen, darunter zählen auch Leerzeichen)",
        help_text="z.B. Ein frisches russisches Gericht mit Paprika, Möhre, Reis und Fleisch",
        )

    def generate(self, input):
        return GeneriereRezept(input).response()
    
    class Meta:
        model = Recipe
        fields = ("text",)
