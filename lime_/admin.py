from django.contrib import admin

from .models import Document, Feature, ClassName

admin.site.register(Document)
admin.site.register(Feature)
admin.site.register(ClassName)