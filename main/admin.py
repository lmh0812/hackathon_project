from django.contrib import admin
from main.models import Bar_code, Upload_Img, Upload_Code, Review, Choice, Upload

from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin

# Register your models here.
class Bar_code_Admin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id','code', 'charge', 'name', 'image', 'pub_date']
    search_fields = ['code', 'name']
    pass

class Choice_Admin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id','code_name', 'choice_text', 'votes']
    search_fields = ['code_name']
    pass

admin.site.register(Bar_code, Bar_code_Admin)

admin.site.register(Upload_Img)
admin.site.register(Upload_Code)
admin.site.register(Review)
admin.site.register(Choice, Choice_Admin)
admin.site.register(Upload)
