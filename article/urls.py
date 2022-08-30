from django.urls import path
from article.views import Article

urlpatterns = [
    path('docType/', Article.as_view()),
]
