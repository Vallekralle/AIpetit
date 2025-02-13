from django.db import models
from django.conf import settings
from django.urls import reverse


class ShoppingList(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=100, 
        verbose_name="Titel für die Einkaufsliste", 
        help_text="z.B. Einkaufsliste für Treffen mit Freunden am 01.01.2025"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("detail_shopping_list", kwargs={"pk": self.pk})


class BulletPoint(models.Model):
    shopping_list = models.ForeignKey(
        ShoppingList,
        on_delete=models.CASCADE
    )
    text = models.TextField(max_length=200)
    marked = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse("detail_bullet_point", kwargs={"pk": self.pk})
