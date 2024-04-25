from django.contrib import admin
from .models import Trainer, Contact
# Register your models here.

admin.site.register((Trainer,Contact))