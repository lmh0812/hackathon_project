from django.contrib import admin
from main.models import Bar_code, Upload_Img, Upload_Code, Review, Choice, Upload

from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin

# Register your models here.
class Bar_code_Admin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Bar_code, Bar_code_Admin)

admin.site.register(Upload_Img)
admin.site.register(Upload_Code)
admin.site.register(Review)
admin.site.register(Choice)
admin.site.register(Upload)
