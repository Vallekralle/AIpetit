from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse

from .models import ShoppingList, BulletPoint


class CreateShoppingListView(LoginRequiredMixin, CreateView):
    model = ShoppingList
    fields = ["title"]
    template_name = "shopping_lists/create_shopping_list.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("detail_shopping_list", args={self.object.id})
    

class DetailShoppingListView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = ShoppingList
    template_name = "shopping_lists/detail_shopping_list.html"

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class DeleteShoppingListView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ShoppingList
    template_name = "shopping_lists/delete_shopping_list.html"

    def get_success_url(self):
        return reverse("list_shopping_lists")

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class ListShoppingLists(LoginRequiredMixin, ListView):
    model = ShoppingList
    template_name = "shopping_lists/list_shopping_lists.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = ShoppingList.objects.filter(user=self.request.user)
        return context
