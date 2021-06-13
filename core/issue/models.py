from django.db import models
from crum import get_current_request
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=191)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ["-id","-created_at"]
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.owner = get_current_request().user
        super(Category, self).save(*args, **kwargs)

class Card(models.Model):
    CARD_STATE = (
        (0, 'OPEN'),
        (1, 'IN PROGRESS'),
        (2, 'CLOSE'),
        (3, 'RE - OPEN'),
    )
    CARD_PRIORITY = (
        (0, 'LOW'),
        (1, 'MEDIUM'),
        (2, 'HIGH'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    summary = models.CharField(max_length=191)
    description = models.TextField(blank=True, null=True)
    priority = models.IntegerField(choices=CARD_PRIORITY)
    state = models.IntegerField(choices=CARD_STATE)
    attachment = models.FileField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    assignee = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='assignee')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = "card"
        verbose_name_plural = "cards"
        ordering = ["state","-priority"]

    def __str__(self):
        return "{} - {}".format(self.category.name.upper(), self.id)

    def get_category(self):
        return "{} - {}".format(self.category.name.upper(), self.id)
    get_category.short_description = "category"

    def save(self, *args, **kwargs):
        self.owner = get_current_request().user
        super(Card, self).save(*args, **kwargs)

class Comment(models.Model):
    note = models.TextField()
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = "comment"
        verbose_name_plural = "comments"
        ordering = ["-id", "-created_at"]

    def save(self, *args, **kwargs):
        self.owner = get_current_request().user
        super(Comment, self).save(*args, **kwargs)

