from django.db import models
from django.urls import reverse


class Website(models.Model):
    hostname = models.CharField(max_length=255)
    url = models.URLField(max_length=255)

    def __str__(self):
        return self.hostname

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
