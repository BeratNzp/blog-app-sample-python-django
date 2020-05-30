from django.urls import path
from . import views

urlpatterns = [
    path('all', views.allArticles, name="allArticles"),
    path('<int:id>/', views.showArticle, name="showArticle"),
    path('<int:id>/comments', views.addComment, name="addComment")
]