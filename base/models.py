from django.db import models
from django.shortcuts import reverse
from django.conf import settings

class Contact(models.Model):
    name = models.CharField(max_length=100, blank=False)
    phone = models.CharField(max_length=100, blank=False)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "контакты"

    def get_absolute_url(self):
        return reverse("get_abs_url_detail", kwargs={"pk": self.pk})
