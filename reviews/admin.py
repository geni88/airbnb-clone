from django.contrib import admin
from . import models


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):

    """review Admin Definition"""

    list_display = ("__str__", "rating_average")
