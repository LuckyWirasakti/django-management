from rest_framework import serializers
from core.issue.models import Card, Category, Comment

class CommentSerializer(serializers.ModelSerializer):
    card = serializers.StringRelatedField()
    owner = serializers.StringRelatedField()
    assignee = serializers.StringRelatedField()
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = [
            "owner",
            "card",
        ]
    
    def create(self, validated_data):
        validated_data["card_id"] = self._kwargs["context"]["request"].parser_context["kwargs"]["card"]
        return super().create(validated_data)

class CardCommentSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()
    class Meta:
        model = Comment
        fields = [
            "id",
            "note",
            "owner"
        ]
class CardDetailSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()
    assignee = serializers.StringRelatedField()
    comment_set = CardCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Card
        exclude = [
            "category"
        ]
        read_only_fields = [
            "summary",
            "description",
            "due_date"
        ]

class CardSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()
    assignee = serializers.StringRelatedField()

    class Meta:
        model = Card
        exclude = [
            "category"
        ]
        read_only_fields = [
            "summary",
            "description",
            "due_date"
        ]

class IssueCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = [
            "id",
            "summary",
        ]

class IssueSerializer(serializers.ModelSerializer):
    card_set = IssueCardSerializer(many=True)
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "card_set",
            "created_at",
            "updated_at"
        ]