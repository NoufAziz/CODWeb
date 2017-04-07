from django.contrib import admin
from .models import Document, Youtube, Quizlet, Pending

admin.site.register(Document)
admin.site.register(Youtube)
admin.site.register(Quizlet)
admin.site.register(Pending)
