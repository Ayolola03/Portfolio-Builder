from django.contrib import admin
from .models import Bio, ContactInfo, CV, SocialLink, Project


@admin.register(Bio)
class BioAdmin(admin.ModelAdmin):
    list_display = ("user", "first_name", "last_name", "created_at", "updated_at")
    search_fields = ("first_name", "last_name", "user__username")
    list_filter = ("created_at", "updated_at")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "user",
                    "first_name",
                    "last_name",
                    "about_me",
                    "profile_picture",
                )
            },
        ),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )
    readonly_fields = ("created_at", "updated_at")


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "email",
        "phone_number",
        "address",
        "created_at",
        "updated_at",
    )
    search_fields = ("email", "phone_number", "user__username")
    list_filter = ("created_at", "updated_at")
    fieldsets = (
        (None, {"fields": ("user", "email", "phone_number", "address")}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )
    readonly_fields = ("created_at", "updated_at")


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ("user", "linkedin", "github", "twitter", "created_at", "updated_at")
    search_fields = ("user__username", "linkedin", "github", "twitter")
    list_filter = ("created_at", "updated_at")
    fieldsets = (
        (None, {"fields": ("user", "linkedin", "github", "twitter")}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )
    readonly_fields = ("created_at", "updated_at")


@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    list_display = ("user", "file", "created_at", "updated_at")
    search_fields = ("user__username",)
    list_filter = ("created_at", "updated_at")
    fieldsets = (
        (None, {"fields": ("user", "file")}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )
    readonly_fields = ("created_at", "updated_at")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "description", "link", "created_at", "updated_at")
    search_fields = ("name", "description", "user__username")
    list_filter = ("created_at", "updated_at")
    fieldsets = (
        (None, {"fields": ("user", "name", "description", "link")}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )
    readonly_fields = ("created_at", "updated_at")
