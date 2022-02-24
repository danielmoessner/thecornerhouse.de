from apps.content.models import Setting, TextSnippet, GalleryImage, ArticleCategory, Job
from apps.content.models import Article
from django.contrib.auth.models import Group
from django.contrib import admin
from django.conf import settings
from django import forms


admin.site.unregister(Group)


class TextSnippetForm(forms.ModelForm):
    class Meta:
        model = TextSnippet
        if settings.DEBUG:
            fields = '__all__'
        else:
            fields = ('text', )

    def __init__(self, *args, **kwargs):
        super(TextSnippetForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['text'].help_text = self.instance.notes


class TextSnippetAdmin(admin.ModelAdmin):
    form = TextSnippetForm

    def has_add_permission(self, request):
        if settings.DEBUG:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if settings.DEBUG:
            return True
        return False


admin.site.register(TextSnippet, TextSnippetAdmin)
admin.site.register(ArticleCategory)
admin.site.register(GalleryImage)
admin.site.register(Setting)
admin.site.register(Article)
# admin.site.register(Job)
