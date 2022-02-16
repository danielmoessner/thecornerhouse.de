from apps.pages.models import Contact, Jobs
from django.contrib import admin
from solo.admin import SingletonModelAdmin

admin.site.register(Contact, SingletonModelAdmin)
admin.site.register(Jobs, SingletonModelAdmin)
