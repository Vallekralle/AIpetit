from django.views import View
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse

from .models import *
from .forms import CommentForm


class TipListView(LoginRequiredMixin, ListView):
    model = Tip
    template_name = "tips/tip_list.html"
    paginate_by = 10


class CreateTipView(LoginRequiredMixin, CreateView):
    model = Tip
    template_name = "tips/create_tip.html"
    fields = ("title", "body", "img")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class CommentGet(DetailView):
    model = Tip
    template_name = "tips/tip_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context


class CommentPost(SingleObjectMixin, FormView):
    model = Tip
    form_class = CommentForm
    template_name = "tips/tip_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        #form.instance.tip = self.request.tip_set
        comment = form.save(commit=False)
        comment.tip = self.object
        comment.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        article = self.get_object()
        return reverse("detail_tip", kwargs={"pk": article.pk})


class DetailTipView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)


class UpdateTipView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Tip
    template_name = "tips/tip_update.html"
    fields = ("title", "body",)
    success_url = reverse_lazy("tip_list")

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class DeleteTipView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Tip
    template_name = "tips/tip_delete.html"
    success_url = reverse_lazy("tip_list")

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user
