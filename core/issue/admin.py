
from core.issue.filters import TrashedListFilter, close_card, re_open_card, soft_delete_card, soft_delete_category
from django.contrib import admin

from core.issue.models import Card, Category, Comment
from rangefilter.filters import DateRangeFilter


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = (
        ("META", {
            "fields": (
                "owner",
                "created_at",
                "updated_at",
                "deleted_at"
            )
        }),
        ("CATEGORY", {
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
        "updated_at"
    )
    actions = (
        soft_delete_category,
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
        "get_category",
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
        "category",
        "state",
        "priority",
    )
    readonly_fields = (
        "owner",
        "created_at",
        "updated_at",
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
            "fields": ("category",)
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

admin.site.register(Category, CategoryAdmin)
admin.site.register(Card, CardAdmin)

