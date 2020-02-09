from django.contrib import admin
from .models import Url, Response

# Register your models here.
admin.site.register(Response)
admin.site.register(Url)
