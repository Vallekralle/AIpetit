from django.db import models
from django.conf import settings
from django.urls import reverse


class Tip(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(blank=False, null=False, max_length=200)
    body = models.TextField(blank=False, null=False)
    likes = models.PositiveIntegerField(default=0)
    img = models.ImageField(upload_to="uploads/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("tip_detail", kwargs={"pk": self.pk})
    
    class Meta:
        ordering = ["likes"]


class Comment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    tip = models.ForeignKey(
        Tip,
        on_delete=models.CASCADE
    )
    body = models.TextField(blank=False, null=False)
    likes = models.PositiveBigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body
    
    def get_absolute_url(self):
        return reverse("tip_list")
    
    
    class Meta:
        ordering = ["likes"]
