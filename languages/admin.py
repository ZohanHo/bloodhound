from django.contrib import admin
from .models import language

class languageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in language._meta.fields]


    class Meta:
        model = language

admin.site.register(language, languageAdmin)

