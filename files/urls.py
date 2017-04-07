from django.conf.urls import url
#from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from files import views

urlpatterns = [
    #url(r'^confirmuploadcompletion/$', TemplateView.as_view(template_name= 'file/confirm_upload_completion.html'), name='confirm_upload_completion'),
    #url(r'^uploadthanks/$', TemplateView.as_view(template_name= 'file/upload_thanks.html'), name='upload_thanks'),
    #url(r'^completionthanks/$', TemplateView.as_view(template_name= 'file/completion_thanks.html'), name='completion_thanks'),
    #url(r'^download/(?P<path>.*)$',  {'document_root': settings.MEDIA_ROOT}),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)