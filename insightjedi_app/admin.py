from django.contrib import admin

from insightjedi_app.models import Document


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'created_time', 'type', 'source_type', 'source_id', 'input_meta_data')
