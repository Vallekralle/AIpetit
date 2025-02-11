from django.views.generic import ListView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.utils import timezone
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.conf import settings

from .forms import RecipeForm
from .models import Recipe


class GenerateRecipeFormView(LoginRequiredMixin, FormView):
    template_name = "recipes/generate_recipe.html"
    form_class = RecipeForm

    def form_valid(self, form):
        recipe_text = form.generate(form.cleaned_data["text"])
        return self.render_to_response(self.get_context_data(form=form, output=recipe_text))

    def get_success_url(self):
        return reverse("generate_recipe")
    

class RecipeListView(ListView):
    template_name = "recipes/list_recipe.html"
    model = Recipe


def SaveRecipeView(request):
    if request.POST:
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
        return HttpResponseRedirect(reverse("my_recipe"))
    return redirect("generate_recipe")