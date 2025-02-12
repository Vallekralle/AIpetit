from django import forms
from django_recaptcha.fields import ReCaptchaField


class EmailForm(forms.Form):
    name = forms.CharField(max_length=100, help_text="z.B. Max Mustermann", label="Dein vollständiger Name")
    email = forms.EmailField(help_text="z.B. maxmustermann@gmail.com", label="Deine Email")
    nachricht = forms.CharField(widget=forms.Textarea, label="Deine Nachricht an uns")
    captcha = ReCaptchaField(label="Bestätige das du ein Mensch bist")