from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import FormMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404

from .models import ShoppingList, BulletPoint
from .forms import BulletPointForm


class CreateShoppingListView(LoginRequiredMixin, CreateView):
    model = ShoppingList
    fields = ["title"]
    template_name = "shopping_lists/create_shopping_list.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("detail_shopping_list", args={self.object.id})
    

class DetailShoppingListView(LoginRequiredMixin, UserPassesTestMixin, FormMixin, DetailView):
    model = ShoppingList
    template_name = "shopping_lists/detail_shopping_list.html"
    form_class = BulletPointForm

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


def DeleteBulletPointView(request, pk):
    bullet_point = get_object_or_404(BulletPoint, id=request.POST.get("bullet_point_id"))
    bullet_point.delete()
    return HttpResponseRedirect(reverse("detail_shopping_list", args=[str(pk)]))


def AddBulletPointView(request, pk):
    if request.POST:
        form = BulletPointForm(request.POST)
        form.instance.shopping_list = get_object_or_404(ShoppingList, id=pk)
        if form.is_valid():
            form.save()
    return HttpResponseRedirect(reverse("detail_shopping_list", args=[str(pk)]))


def CheckBulletPointView(request, pk):
    bullet_point = get_object_or_404(BulletPoint, id=request.POST.get("bullet_point_id"))
    if bullet_point.marked:
        bullet_point.marked = False
    else:
        bullet_point.marked = True
    bullet_point.save()

    return HttpResponseRedirect(reverse("detail_shopping_list", args=[str(pk)]))


def EditBulletPointView(request, pk):
    if request.POST:
        form = BulletPointForm(request.POST)
        form.instance.shopping_list = get_object_or_404(ShoppingList, id=pk)
        
        if form.is_valid():
            bullet_point = get_object_or_404(BulletPoint, id=request.POST.get("bullet_point_id"))
            bullet_point.text = form.cleaned_data["text"]
            bullet_point.save()

    return HttpResponseRedirect(reverse("detail_shopping_list", args=[str(pk)]))