from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "pages/index.html"


class LearnMoreView(TemplateView):
    template_name = "pages/learn_more.html"


class AboutUsView(TemplateView):
    template_name = "pages/about_us.html"


class DataProtectionView(TemplateView):
    template_name = "pages/data_protection.html"


class ImprintView(TemplateView):
    template_name = "pages/imprint.html"


class ContactView(TemplateView):
    template_name = "pages/contact.html"
