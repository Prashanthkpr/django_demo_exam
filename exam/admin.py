from django.contrib import admin

from exam.models import *

# Register your models here.

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Tag)
