from django.db import models

class FileQuerySet(models.QuerySet):
    def to_user(self, user):
        return self.filter(file_submitter=user)
    def by_user(self, user):
        return self.filter(requester=user)

    def make_submitted(modeladmin, request, queryset):
        queryset.update(status='SUB')
    def make_published(modeladmin, request, queryset):
        queryset.update(status='PUB')
    def make_rejected(modeladmin, request, queryset):
        queryset.update(status='REJ')
