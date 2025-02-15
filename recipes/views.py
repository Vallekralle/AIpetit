from django.views.generic import ListView, FormView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse

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
    

class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = "recipes/list_recipe.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Recipe.objects.filter(user=self.request.user)
        return context
    

class RecipeDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Recipe
    template_name = "recipes/detail_recipe.html"

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class DeleteRecipeView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    template_name = "recipes/delete_recipe.html"

    def get_success_url(self):
        return reverse("my_recipe")
    
    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


def SaveRecipeView(request):
    if request.POST:
        form = RecipeForm(request.POST)
        form.instance.user = request.user
        
        if form.is_valid():
            form.save()

        return HttpResponseRedirect(reverse("my_recipe"))
    return redirect("generate_recipe")