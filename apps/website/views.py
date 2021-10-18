from django.views.generic.edit import FormMixin
from django.views.generic import TemplateView
from apps.content.models import ArticleCategory, TextSnippet, GalleryImage, Setting, Article, Member
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.urls import reverse_lazy
from datetime import timedelta, datetime
from .models import StaticPage, CustomCode, Seo
from .forms import ContactForm


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
        context['article_categories'] = ArticleCategory.objects.filter(featured=True)
        context['article_categories_index'] = context['article_categories'][:3]
        context['text_snippets'] = TextSnippet.get_dict('startseite')
        context['events'] = Article.objects.filter(date__gte=datetime.now() - timedelta(days=30),
                                                   category__name='Veranstaltungen')
        context['settings'] = Setting.get_dict('startseite')
        return context


class ContactView(FormMixin, WebsiteView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('website:contact_mail_sent')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article_categories'] = ArticleCategory.objects.filter(featured=True)
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
                'Datum: {date}<br>'
                'Uhrzeit: {time}<br>'
                'Ort: {location}<br>'
                'Kommentar: {comment}<br>'
            ).format(**form.cleaned_data)
            from_mail = '{email}'.format(**form.cleaned_data)
            recipient_list = ['ammadi@hotmail.de', 'happy@apps.de']
            send_mail(subject, message, from_mail, recipient_list, html_message=message)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class ThanksView(WebsiteView):
    template_name = 'thanks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article_categories'] = ArticleCategory.objects.filter(featured=True)
        context['text_snippets'] = TextSnippet.get_dict(page='danke')
        return context


class MenuView(WebsiteView):
    template_name = 'menu_new.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article_categories'] = ArticleCategory.objects.filter(featured=True)
        context['text_snippets'] = TextSnippet.get_dict(page='menue')
        # context['menu'] = {}
        # for category in MenuCategory.objects.all().prefetch_related('menu_entries'):
        #     category_data = []
        #     for menu_entry in category.menu_entries.all():
        #         ppq_data = {}
        #         for ppq in menu_entry.ppqs.order_by('unit', '-content', 'price'):
        #             ppq_data = {'content': ppq.content, 'unit': ppq.unit, 'price': ppq.price}
        #             break
        #         category_data.append({'name': menu_entry.name, 'description': menu_entry.description, 'ppq': ppq_data})
        #     category_half = int((category.menu_entries.count() + 1) / 2)
        #     context['menu'][category.name] = {'content': [category_data[:category_half], category_data[category_half:]],
        #                                       'img': category.image.url}

        return context


# class MenuListView(WebsiteView):
#     template_name = 'menu_list.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         context['menu'] = {}
#         for category1 in MenuCategory1.objects.all():
#             category1_data = {}
#             for category2 in category1.categories.all():
#                 category2_data = []
#                 for menu_entry in category2.menu_entries.all().prefetch_related('ppqs', 'additives'):
#                     additive_data = []
#                     for additive in menu_entry.additives.order_by('number'):
#                         additive_data.append(additive.number)
#                     ppq_data = []
#                     for ppq in menu_entry.ppqs.order_by('unit', 'content', 'price'):
#                         ppq_data.append({'content': ppq.content, 'unit': ppq.unit, 'price': str(ppq.price) + ' €'})
#                     if len(ppq_data) == 1:
#                         ppq_data.insert(0, {'content': '', 'unit': '', 'price': ''})
#                     category2_data.append({'name': menu_entry.name, 'description': menu_entry.description,
#                                           'additives': additive_data, 'ppqs': ppq_data})
#                 category1_data[category2.name] = category2_data
#             context['menu'][category1.name] = category1_data
#
#         context['additives'] = MenuAdditive.objects.all()
#         return context


class BlogView(WebsiteView):
    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.all().select_related('category')
        if 'slug' in kwargs:
            context['article_category'] = get_object_or_404(ArticleCategory, slug=kwargs['slug'])
            context['articles'] = context['articles'].filter(category=context['article_category'])
        context['article_categories'] = ArticleCategory.objects.filter(featured=True)
        return context


class StaticPageView(WebsiteView):
    template_name = 'static.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'slug' in kwargs:
            context['static_page'] = get_object_or_404(StaticPage, slug=kwargs['slug'])
        context['article_categories'] = ArticleCategory.objects.filter(featured=True)
        return context


class ArticleView(WebsiteView):
    template_name = 'article.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'slug' in kwargs:
            context['article'] = get_object_or_404(Article, slug=kwargs['slug'])
        context['article_categories'] = ArticleCategory.objects.filter(featured=True)
        context['recent_articles'] = Article.objects.order_by('-date')[:3]
        return context


class AboutView(WebsiteView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article_categories'] = ArticleCategory.objects.filter(featured=True)
        context['members'] = Member.objects.all()
        context['text_snippets'] = TextSnippet.get_dict(page='ueber-uns')
        return context
