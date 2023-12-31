from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Sample(models.Model):
    char_field = models.CharField(_("char field"), max_length=50)

    class Meta:
        verbose_name = _("Sample")
        verbose_name_plural = _("Samples")

    def __str__(self):
        return self.name
