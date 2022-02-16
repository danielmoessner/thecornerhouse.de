from django.urls import path
from django.views.generic import RedirectView

from . import views


app_name = "website"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('kontakt/', views.ContactView.as_view(), name='contact'),
    path('kontakt/danke/', views.ContactThanksView.as_view(), name='contact_mail_sent'),
    path('menue/', views.MenuView.as_view(), name='menu'),
    path('ueber-uns/', views.AboutView.as_view(), name='about'),
    path('jobs/', views.JobsView.as_view(), name='jobs'),
    path('jobs/danke/', views.JobsThanksView.as_view(), name='jobs_mail_sent'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('blog/artikel/<slug:slug>/', views.ArticleView.as_view(), name='article'),
    path('blog/<slug:slug>/', views.BlogView.as_view(), name='article_category'),
    path('seite/<slug:slug>/', views.StaticPageView.as_view(), name='static_page'),
    # other or old stuff
    path('article/<slug:slug>/', RedirectView.as_view(pattern_name='website:article', permanent=True)),
]
