from django.urls import path
from article.views import Article

urlpatterns = [
    path('catagory/', Article.as_view()),
]
