from django.contrib import admin
from django.utils.safestring import mark_safe

from . import models


class ProfileAdmin(admin.ModelAdmin):

    list_display = ('id', 'user', 'contacts', 'image', 'birth_date')
    list_filter = (
        'user',
        'birth_date',
        'id',
        'user',
        'contacts',
        'image',
        'birth_date',
    )




class VideodashAdmin(admin.ModelAdmin):

    list_display = ('id', 'titre','url_video', 'statut', 'date_Add', 'date_Upd')
    list_filter = (
        'statut',
        'date_Add',
        'date_Upd',
        'id',
        'titre',
        'url_video',
        'statut',
        'date_Add',
        'date_Upd',
    )

    # def affichevideo(self, objec):
    #     return mark_safe('<iframe width="200" height="150" src="{url}"></iframe>'.format(url=objec.url_video.url))


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Profile, ProfileAdmin)
_register(models.Videodash, VideodashAdmin)
