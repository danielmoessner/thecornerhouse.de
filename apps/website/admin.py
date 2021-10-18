from django.contrib import admin
from .models import Seo
from .models import CustomCode
from .models import StaticPage

admin.site.register(Seo)
admin.site.register(CustomCode)
admin.site.register(StaticPage)
