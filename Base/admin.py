import csv
from django.contrib.admin import AdminSite
from django.contrib import admin
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _
from django.db.models import Q
from .models import *


# Register your models here.

class InputFilter(admin.SimpleListFilter):
    template = 'admin/input_filter.html'

    def lookups(self, request, model_admin):
        return (
            ('store', _('Store')),
        )


class StoreFilter(InputFilter):
    parameter_name = 'store'
    title = _('Store')

    def queryset(self, request, queryset):
        if self.value() is not None:
            uid = self.value()
            return queryset.filter(
                Q(store=uid)
            )


class PageAdmin(admin.ModelAdmin):
    list_filter = [StoreFilter]
    list_display = ['store', 'model', 'sitetype', 'podnumber']


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"




class StoreAdmin(ExportCsvMixin, PageAdmin):
    model = Siteinventory
    actions = ["export_as_csv"]
    list_display = ['store', 'model', 'sitetype', 'podnumber']


class Meta:
    model = Siteinventory


admin.site.register(Siteinventory, StoreAdmin)
