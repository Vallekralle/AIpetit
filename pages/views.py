from django.views.generic import TemplateView, FormView
from django.core.mail import send_mail

from .forms import EmailForm


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


class ContactView(FormView):
    template_name = "pages/contact.html"
    form_class = EmailForm

    def form_valid(self, form):
        content = f"""
                Email von: {form.cleaned_data["email"]}\n
                {form.cleaned_data["nachricht"]}
        """

        send_mail(
            f"{form.cleaned_data['name']} - Email von AIpetit",
            content,
            "kunzvalentin4@gmail.com",
            ['kunzvalentin4@gmail.com'],
            fail_silently=False,
        )
        return self.render_to_response(
            self.get_context_data(
                form=EmailForm(), output="Ihre Email wurde erfolgreich versendet!"
                )
            )   
