from django.db import models


class RefreshToken(models.Model):
    key = models.CharField(max_length=5, unique=True, primary_key=True)
    value = models.JSONField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Gmail OAuth Refresh Token'
        verbose_name_plural = 'Gmail OAuth Refresh Tokens'