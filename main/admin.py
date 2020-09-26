from django.contrib import admin
from main.models import Bar_code, Upload_Img, Upload_Code, Review, Choice, Upload

# Register your models here.

admin.site.register(Bar_code)
admin.site.register(Upload_Img)
admin.site.register(Upload_Code)
admin.site.register(Review)
admin.site.register(Choice)
admin.site.register(Upload)
