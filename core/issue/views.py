from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.filters import SearchFilter
from core.issue.filters import CardByIssueFilterBackend, CommentByCardFilterBackend
from core.issue.models import Card, Project, Comment
from django_filters.rest_framework import DjangoFilterBackend
from core.issue.serializers import CardDetailSerializer, CardSerializer, CommentSerializer, IssueSerializer

# Create your views here.
class IssueList(ListAPIView):
    serializer_class = IssueSerializer
    queryset = Project.objects.all()
    filter_backends = [
        SearchFilter,
    ]
    search_fields = [
        "name",
        "card__summary",
        "card__description"
    ]
    

class IssueDetail(RetrieveAPIView):
    serializer_class = IssueSerializer
    queryset = Project.objects.all()
    
class CardList(ListAPIView):
    serializer_class = CardSerializer
    queryset = Card.objects.all()
    filter_backends = [
        CardByIssueFilterBackend,
        DjangoFilterBackend,
    ]

class CardDetail(RetrieveAPIView, UpdateAPIView):
    serializer_class = CardDetailSerializer
    queryset = Card.objects.all()

class CommentList(ListAPIView,CreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    filter_backends = [
        CommentByCardFilterBackend
    ]