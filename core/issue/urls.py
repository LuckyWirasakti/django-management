from core.issue.views import CardDetail, CardList, CommentList, IssueDetail, IssueList
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path("token", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify", TokenVerifyView.as_view(), name="token_verify"),
    path("issues", IssueList.as_view(), name="issue-list"),
    path("issues/<int:pk>", IssueDetail.as_view(), name="issue-detail"),
    path("cards/<int:project>/issue", CardList.as_view(), name="card-list"),
    path("cards/<int:pk>", CardDetail.as_view(), name="card-detail"),
    path("comments/<int:card>/card", CommentList.as_view(), name="comment-list"),
]