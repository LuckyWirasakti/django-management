
from core.issue.filters import TrashedListFilter, close_card, re_open_card, soft_delete_card, soft_delete_project
from django.contrib import admin

from core.issue.models import Card, Project, Comment
from rangefilter.filters import DateRangeFilter


class ProjectAdmin(admin.ModelAdmin):
    fieldsets = (
        ("META", {
            "fields": (
                "owner",
                "created_at",
                "updated_at",
                "deleted_at"
            )
        }),
        ("PROJECT", {
            "fields": ("name",)
        })
    )
    search_fields = (
        "name",
    )
    list_display = (
        "id",
        "name",
        "created_at",
        "updated_at",
    )
    date_hierarchy = (
        "created_at"
    )
    readonly_fields = (
        "owner",
        "created_at",
        "updated_at",
        "deleted_at",
    )
    actions = (
        soft_delete_project,
    )
    list_filter = (
        TrashedListFilter,
    )
    
class CommentInline(admin.TabularInline):
    model = Comment
    readonly_fields = (
        "owner",
        "created_at",
        "updated_at"
    )
    extra = 0



class CardAdmin(admin.ModelAdmin):
    actions = (
        re_open_card,
        close_card,       
        soft_delete_card,       
    )
    search_fields = (
        "summary",
        "description",
    )
    list_editable = (
        "state",
        "priority"
    )
    list_display = (
        "id",
        "get_project",
        "summary",
        "priority",
        "state",
        "created_at",
        "updated_at",
    )
    date_hierarchy = (
        "created_at"
    )
    list_filter = (
        ("created_at", DateRangeFilter),
        TrashedListFilter,
        "project",
        "state",
        "priority",
    )
    readonly_fields = (
        "owner",
        "created_at",
        "updated_at",
        "deleted_at",
    )
    inlines = (
        CommentInline,
    )
    fieldsets = (
        ("META", {
            "fields": (
                "owner",
                "created_at",
                "updated_at",
                "deleted_at"
            )
        }),
        ("NEW ISSUE IN", {
            "fields": ("project",)
        }),
        ("CARD", {
            "fields": (
                "summary",
                "priority",
                "state", 
                "assignee",
                "description",
            )
        }),
        ("ADVANCED OPTIONS", {
            "classes": ("collapse",),
            "fields": (
                "due_date",
                "attachment",
            ),
        }),
    )
    list_per_page = 10

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "project":
            kwargs["queryset"] = Project.objects.filter(deleted_at__isnull=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Project, ProjectAdmin)
admin.site.register(Card, CardAdmin)

