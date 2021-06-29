from django.contrib import admin

from .models import ProducerProfile, CustomerProfile

admin.site.register(ProducerProfile)
admin.site.register(CustomerProfile)

