from django.db import models
from django.conf import settings
from django.urls import reverse


class Recipe(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text[:50]}..." if len(self.text) > 50 else self.text
    
    def get_absolute_url(self):
        return reverse("recipe_detail", kwargs={"pk": self.pk})
