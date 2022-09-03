from django.urls import path
from apps.views import Article

urlpatterns = [
    path('docType/', Article.as_view()),
]
