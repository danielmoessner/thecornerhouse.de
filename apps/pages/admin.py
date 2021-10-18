from apps.pages.models import Contact
from django.contrib import admin

from solo.admin import SingletonModelAdmin

admin.site.register(Contact, SingletonModelAdmin)
