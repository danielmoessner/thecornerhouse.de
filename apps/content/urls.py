from django.urls import re_path
from apps.content import views

app_name = "core"
urlpatterns = [
    re_path(r'^(?!static).*(js|images|css|fonts).*$', views.StaticRedirectView.as_view(), name='static_redirect')
]
