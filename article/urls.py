from django.urls import path
from article.views import Article

urlpatterns = [
    path('', Article.as_view()),
]
