from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.db import models

# Missing SOURCE_CHOICES detail in your sheet, so I created dummy
SOURCE_CHOICES = (
        ("Customer", "Customer"),
        ("Employee", "Employee"),
)


class Document(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="exports")
    created_time = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=100)
    source_type = models.CharField( max_length=20, choices=SOURCE_CHOICES, blank=True, null=True)
    source_id = models.CharField(max_length=50, blank=True, null=True)
    input_meta_data = JSONField(default=dict, blank=True, null=True)
