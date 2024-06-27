from django.db import models
from django.utils.translation import gettext_lazy
from django.utils import timezone


class BaseModel(models.Model):
    name: str

    created = models.DateTimeField(
        default=timezone.now,
        verbose_name=gettext_lazy('created'),
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name=gettext_lazy('updated'),
    )

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
