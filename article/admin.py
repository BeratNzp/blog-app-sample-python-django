from django.contrib import admin

# Register your models here.
from .models import Article,Category,Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title"]
    class Meta:
        model = Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ["title","author","created_date"]
    list_display_links = ["title","created_date"]

    search_fields = ["title"]
    list_filter = ["created_date"]

    class Meta:
        model = Article

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ["article","content","author","created_date"]

    search_fields = ["content"]
    list_filter = ["created_date"]

    class Meta:
        model = Comment