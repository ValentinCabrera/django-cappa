from django.db import models
from django.core.validators import MinLengthValidator
class Setting(models.Model):
    background_color = models.CharField(max_length=6, validators=[MinLengthValidator(6)])

    def __str__(self):
        return ("Settings")