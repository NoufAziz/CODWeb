from core import views
from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.index, name='index'),
#    url(r'^contact/$', TemplateView.as_view(template_name= 'contact.html'), name='contact'),
#    url(r'^about/$', TemplateView.as_view(template_name= 'about.html'), name='about'),
    url(r'^categories/(?P<slug>[\d\w_]+)/$', views.show_category, name='show_category'),
    url(r'^subject/(?P<pk>\d+)/$', views.show_subject, name='show_subject'),
]