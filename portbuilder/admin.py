from django.contrib import admin
from .models import Bio, ContactInfo, SocialLink, CV, Project, Stack, Services, work_exp


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ("user", "platform", "url", "created_at", "updated_at")
    search_fields = ("user__username", "platform", "url")
    list_filter = ("platform", "created_at", "updated_at")
    fieldsets = (
        (None, {"fields": ("user", "platform", "url")}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )
    readonly_fields = ("created_at", "updated_at")


@admin.register(Bio)
class BioAdmin(admin.ModelAdmin):
    list_display = ("user", "first_name", "last_name", "role", "created_at", "updated_at")
    search_fields = ("user__username", "first_name", "last_name")
    list_filter = ("created_at", "updated_at")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "user",
                    "first_name",
                    "last_name",
                    "role",
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
    search_fields = ("user__username", "email", "phone_number", "address")
    list_filter = ("created_at", "updated_at")
    fieldsets = (
        (None, {"fields": ("user", "email", "phone_number", "address")}),
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
    list_display = ("user", "name", "link", "created_at", "updated_at")
    search_fields = ("user__username", "name", "link")
    list_filter = ("created_at", "updated_at")
    fieldsets = (
        (None, {"fields": ("user", "name", "description", "link")}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )
    readonly_fields = ("created_at", "updated_at")


@admin.register(Stack)
class StackAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "mastery_level", "experience_years")
    search_fields = ("user__username", "name", "mastery_level")
    list_filter = ("mastery_level", "experience_years")
    fieldsets = (
        (None, {"fields": ("user", "name", "mastery_level", "experience_years")}),
    )


@admin.register(Services)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("user", "name")
    search_fields = ("user__username", "name")
    list_filter = ("name",)
    fieldsets = ((None, {"fields": ("user", "name", "description", "price")}),)

@admin.register(work_exp)
class WorkExpAdmin(admin.ModelAdmin):
    list_display = ("work_done", "Company", "start_date", "end_date")
    search_fields = ("work_done", "Company")
    list_filter = ("work_done", "Company")
    
