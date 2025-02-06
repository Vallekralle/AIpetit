from django.db import models
from django.conf import settings


class Tip(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(blank=False, null=False, max_length=200)
    body = models.TextField(blank=False, null=False)
    likes = models.PositiveIntegerField()
    img = models.ImageField(upload_to="uploads/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
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
    likes = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body
    
    class Meta:
        ordering = ["likes"]
