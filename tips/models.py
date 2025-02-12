from django.db import models
from django.conf import settings
from django.db.models import Count
from django.urls import reverse


class TipManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().annotate(like_count=Count("likes")).order_by("-like_count", "-created_at")

class Tip(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(blank=False, null=False, max_length=200,
                            verbose_name ="Titel", help_text="Ein aussagekräftiger Titel")
    body = models.TextField(blank=False, null=False, verbose_name ="Text", help_text="Ausführliche Erklärung deines Tipps")
    img = models.ImageField(upload_to="uploads/", null=True, blank=False, verbose_name ="Bild", help_text="Inhaltsstarkes Bild zu deinem Tipp")
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_posts")

    objects = TipManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail_tip", kwargs={"pk": self.pk})
    
    class Meta:
        ordering = ["created_at"]


class CommentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().annotate(like_count=Count("likes")).order_by("-like_count", "-created_at")
    

class Comment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    tip = models.ForeignKey(
        Tip,
        on_delete=models.CASCADE
    )
    body = models.TextField(blank=False, null=False, verbose_name ="Kommentar", help_text="Kommentar schreiben (bitte keine Beleidigungen)")
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_comments")

    objects = CommentManager()

    def __str__(self):
        return self.body
    
    def get_absolute_url(self):
        return reverse("tip_list")
    
    class Meta:
        ordering = []
