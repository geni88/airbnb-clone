from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# admin.site.register(models.User, CustomUserAdmin) 과 밑에 것은 동일한 것~~
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """Custom User Admin"""

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )

    list_filter = UserAdmin.list_filter + ("superhost",)

    list_display = (
        "username",
        "email",
        "is_active",
        "language",
        "superhost",
        "is_staff",
        "is_superuser",
    )
