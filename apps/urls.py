from django.urls import path
from apps.views import Article

urlpatterns = [
    path('', Article.as_view()),
]
