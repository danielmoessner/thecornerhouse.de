from django.http import HttpResponseRedirect
from django.views.generic.edit import FormMixin
from django.views.generic import TemplateView
from apps.content.models import ArticleCategory, TextSnippet, GalleryImage, Setting, Article, Job
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail, EmailMessage
from django.urls import reverse_lazy, reverse
from datetime import timedelta, datetime
from .models import StaticPage, CustomCode, Seo
from .forms import ContactForm, JobForm


class WebsiteView(TemplateView):

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.slug = request.get_full_path()

    def get_seo_data(self):
        seos = []
        for seo in Seo.objects.all():
            if seo.url in self.slug:
                seos.append(seo)

        if not seos:
            seo = Seo.objects.filter(url='').first()
            if seo:
                return {'title': seo.title_tag, 'description': seo.meta_description}
            else:
                return {'title': 'No title yet.', 'description': 'No description yet.'}

        final_seo = None
        slug_length = -1
        for seo in seos:
            seo_slug_length = len(seo.url)
            if seo_slug_length > slug_length:
                final_seo = seo
                slug_length = seo_slug_length

        return {'title': final_seo.title_tag, 'description': final_seo.meta_description}

    def get_custom_code(self):
        header_code = ''
        footer_code = ''
        custom_codes = []
        for custom_code in CustomCode.objects.all():
            cc_slug = custom_code.url
            if cc_slug == '' or cc_slug in self.slug:
                custom_codes.append(custom_code)
        for custom_code in custom_codes:
            if custom_code.location == 'HEAD':
                header_code += custom_code.code
            else:
                footer_code += custom_code.code
        return {'header_code': header_code, 'footer_code': footer_code}

    def get_static_pages(self):
        static_pages_footer = StaticPage.objects.filter(shown_in_footer=True)
        static_pages_navigation = StaticPage.objects.filter(shown_in_navigation=True)
        static_pages = StaticPage.objects.all()
        return {'static_pages_footer': static_pages_footer, 'static_pages_navigation': static_pages_navigation,
                'static_pages': static_pages}

    def get_gallery_data(self):
        index_images = list(GalleryImage.objects.filter(featured_on_index=True))
        if 0 < len(index_images):
            while len(index_images) < 5:
                index_images += index_images[:5 - len(index_images)]
        about_images = list(GalleryImage.objects.filter(featured_on_about=True))
        if 0 < len(about_images):
            while len(about_images) < 5:
                about_images += about_images[:5 - len(about_images)]
        return {'index_gallery': index_images, 'about_gallery': about_images}

    def get_setting_data(self):
        return {'settings_general': Setting.get_dict('allgemein')}

    def get_general_information(self):
        return {'text_snippets_general': TextSnippet.get_dict('allgemein')}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_seo_data())
        context.update(self.get_custom_code())
        context.update(self.get_static_pages())
        context.update(self.get_gallery_data())
        context.update(self.get_general_information())
        context.update(self.get_setting_data())
        return context


class IndexView(WebsiteView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article_categories'] = ArticleCategory.objects.all()
        context['article_categories_index'] = ArticleCategory.objects.filter()[:3]
        context['text_snippets'] = TextSnippet.get_dict('startseite')
        context['events'] = Article.objects.filter(date__gte=datetime.now() - timedelta(days=30),
                                                   category__name='Veranstaltungen', show=True)
        context['settings'] = Setting.get_dict('startseite')
        return context


class ContactView(FormMixin, WebsiteView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('website:contact_mail_sent')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article_categories'] = ArticleCategory.objects.filter()
        context['text_snippets'] = TextSnippet.get_dict(page='kontakt')
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            subject = 'Reservierung'
            message = (
                'Name: {name}<br>'
                'E-Mail: {email}<br>'
                'Telefon: {phone}<br>'
                'Anzahl Personen: {persons}<br>'
                'Datum und Uhrzeit: {datetime}<br>'
                'Ort: {location}<br>'
                'Kommentar: {comment}<br>'
            ).format(**form.cleaned_data)
            reply_email = '{email}'.format(**form.cleaned_data)
            from_email = 'happy@thecornerhouse.de'
            recipient_list = ['ammadi@hotmail.de', 'happy@thecornerhouse.de']
            msg = EmailMessage(subject, message, from_email, recipient_list, reply_to=[reply_email])
            msg.content_subtype = "html"
            msg.send()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class ContactThanksView(WebsiteView):
    template_name = 'contact_thanks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article_categories'] = ArticleCategory.objects.filter()
        context['text_snippets'] = TextSnippet.get_dict(page='danke')
        return context


class MenuView(WebsiteView):
    template_name = 'menu.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article_categories'] = ArticleCategory.objects.filter()
        context['text_snippets'] = TextSnippet.get_dict(page='menue')
        return context


class BlogView(WebsiteView):
    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.filter(show=True).select_related('category')
        if 'slug' in kwargs:
            context['article_category'] = get_object_or_404(ArticleCategory, slug=kwargs['slug'])
            context['articles'] = context['articles'].filter(category=context['article_category'])
        context['article_categories'] = ArticleCategory.objects.filter()
        return context


class StaticPageView(WebsiteView):
    template_name = 'static.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'slug' in kwargs:
            context['static_page'] = get_object_or_404(StaticPage, slug=kwargs['slug'])
        context['article_categories'] = ArticleCategory.objects.filter()
        return context


class ArticleView(FormMixin, WebsiteView):
    template_name = 'article.html'
    form_class = JobForm
    success_url = reverse_lazy('website:jobs_mail_sent')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'slug' in kwargs:
            context['article'] = get_object_or_404(Article, slug=kwargs['slug'])
        context['article_categories'] = ArticleCategory.objects.filter()
        context['recent_articles'] = Article.objects.filter(show=True).order_by('-date')[:3]
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            subject = 'Job'
            message = (
                'Job: {job}<br>'
                'Name: {name}<br>'
                'E-Mail: {email}<br>'
                'Telefon: {phone}<br>'
                'Inhalt: <br>{content}<br>'
            ).format(**form.cleaned_data)
            from_mail = '{email}'.format(**form.cleaned_data)
            recipient_list = ['ammadi@hotmail.de', 'happy@thecornerhouse.de']
            send_mail(subject, message, from_mail, recipient_list, html_message=message)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class AboutView(WebsiteView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article_categories'] = ArticleCategory.objects.filter()
        context['text_snippets'] = TextSnippet.get_dict(page='ueber-uns')
        return context


class JobsView(FormMixin, WebsiteView):
    template_name = 'jobs.html'
    form_class = JobForm
    success_url = reverse_lazy('website:jobs_mail_sent')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jobs'] = Job.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            subject = 'Job'
            message = (
                'Job: {job}<br>'
                'Name: {name}<br>'
                'E-Mail: {email}<br>'
                'Telefon: {phone}<br>'
                'Inhalt: <br>{content}<br>'
            ).format(**form.cleaned_data)
            from_mail = '{email}'.format(**form.cleaned_data)
            recipient_list = ['ammadi@hotmail.de', 'happy@thecornerhouse.de']
            send_mail(subject, message, from_mail, recipient_list, html_message=message)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class JobsThanksView(WebsiteView):
    template_name = 'jobs_thanks.html'
