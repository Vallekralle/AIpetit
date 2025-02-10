from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from .forms import RecipeForm


class GenerateRecipeTemplateView(LoginRequiredMixin, FormView):
    template_name = "recipes/generate_recipe.html"
    form_class = RecipeForm

    def form_valid(self, form):
        recipe_text = form.generate(form.cleaned_data["text"])
        return self.render_to_response(self.get_context_data(form=form, output=recipe_text))

    def get_success_url(self):
        return reverse("generate_recipe")
