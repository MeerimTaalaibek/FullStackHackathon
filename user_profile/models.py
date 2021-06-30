from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class ProducerProfile(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE, related_name='producer_profile')
    email = models.EmailField(max_length=255, unique=True)
    country = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        to_slug = str(self.name)
        self.slug = to_slug
        super().save(*args, **kwargs)


class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_prof')
    email = models.EmailField(max_length=255, unique=True)
    country = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        to_slug = str(self.user)
        self.slug = to_slug
        super().save(*args, **kwargs)
