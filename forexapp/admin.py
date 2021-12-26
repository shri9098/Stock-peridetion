from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export.fields import Field
from forexapp.models import *

class HistryDataResource(resources.ModelResource):

    class Meta:
        model = TradingData
        Date = Field(attribute='Date', column_name='date')
        Price = Field(attribute='Price', column_name='price')
        Open = Field(attribute='Open', column_name='open_price')
        High = Field(attribute='High', column_name='high')
        Low = Field(attribute='Low', column_name='low')
        change_percentage = Field(attribute='Change%', column_name='change_percentage')
        widgets = {
                'date': {'format': '%b %d, %Y'},
                }

class TradingDataAdmin(ImportExportModelAdmin):
    resource_class = HistryDataResource

admin.site.register(TradingData, TradingDataAdmin)


admin.site.register(PredictionData)
admin.site.register(Currencies)
admin.site.register(UserHistory)
admin.site.register(NotifyData)
