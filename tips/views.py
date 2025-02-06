from django.views.generic import ListView


from .models import *


class TipListView(ListView):
    model = Tip
    template_name = "tips/tips.html"
