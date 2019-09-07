from django.db import models


class User(models.Model):
    id = models.BigAutoField(blank=False, null=False, primary_key=True)
    name = models.CharField(blank=False, null=False, max_length=255)
    email = models.CharField(blank=True, null=True, max_length=255)
    profile = models.CharField(max_length=255)

    class Meta:
        db_table = 'user'
