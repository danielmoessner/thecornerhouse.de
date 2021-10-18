from django.views.generic import RedirectView
from django.http import HttpResponseRedirect
import re


class StaticRedirectView(RedirectView):
    def get(self, request, *args, **kwargs):
        current_url = request.get_full_path()
        splitted_url = re.split(r'(js|images|css)', current_url)
        url = ''.join(splitted_url[1:])
        static_url = '/static/' + url
        return HttpResponseRedirect(static_url)
