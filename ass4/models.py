from django_otp.plugins.otp_totp.models import TOTPDevice
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, URLValidator
from encrypted_model_fields.fields import EncryptedCharField


class CustomTOTPDevice(TOTPDevice):
    pass

class SecureData(models.Model):
    name = EncryptedCharField(max_length=100)  # Поле будет зашифровано
    age = models.PositiveIntegerField(validators=[MinValueValidator(18), MaxValueValidator(120)])
    website = models.URLField()

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)