from django.urls import path
from article.views import *

app_name = 'article'

urlpatterns = [
    path('dashboard/', dashboard, name = "dashboard"),
    path('addarticle/', addArticle, name = "addarticle"),
    path('article/<int:id>', detail, name = "detail"),
    path('update/<int:id>', updateArticle, name = "update"),
    path('delete/<int:id>', deleteArticle, name = "delete"),
    path('', articles, name = "articles"),
    path('comment/<int:id>', addComment, name = "comment"),
]