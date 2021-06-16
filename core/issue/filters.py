from rest_framework import filters
from django.utils import timezone
from django.contrib import admin
from django.db.models import Q

class CardByIssueFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(project=view.kwargs.get('project', None))

class CommentByCardFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(card=view.kwargs.get('card', None))

class TrashedListFilter(admin.SimpleListFilter):
    title = "Trashed List"
    parameter_name = "trashed"
    def lookups(self, request, model_admin):
        return ((1, "Trashed List"),)

    def queryset(self, request, queryset):
        if self.value() == '1':
            return queryset
        return queryset.filter(deleted_at__isnull=True)

@admin.action(description="Soft delete selected projects")
def soft_delete_project(modeladmin, request, queryset):
    queryset.update(deleted_at=timezone.now())

@admin.action(description="Re Open selected cards")
def re_open_card(modeladmin, request, queryset):
    queryset.update(state=3)

@admin.action(description="Close selected cards")
def close_card(modeladmin, request, queryset):
    queryset.update(state=2)

@admin.action(description="Soft delete selected cards")
def soft_delete_card(modeladmin, request, queryset):
    queryset.update(deleted_at=timezone.now())