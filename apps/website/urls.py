from django.urls import path
from . import views


app_name = "website"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('kontakt/', views.ContactView.as_view(), name='contact'),
    path('danke/', views.ThanksView.as_view(), name='contact_mail_sent'),
    path('menue/', views.MenuView.as_view(), name='menu'),
    path('events/', views.IndexView.as_view(), name='events'),
    path('neuigkeiten/', views.IndexView.as_view(), name='news'),
    path('biere/', views.IndexView.as_view(), name='beers'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('article/<slug:slug>', views.ArticleView.as_view(), name='article'),
    path('ueber-uns/', views.AboutView.as_view(), name='about'),
    path('blog/<slug:slug>', views.BlogView.as_view(), name='article_category'),
    path('seite/<slug:slug>', views.StaticPageView.as_view(), name='static_page'),
    # path('menue-liste', views.MenuListView.as_view(), name='menu_list')
]
