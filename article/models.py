from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import MinLengthValidator

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=64, verbose_name="Kategori Başlığı")
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['title']

class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Yazar")
    category = models.ForeignKey(Category, null=True, on_delete=models.PROTECT, verbose_name="Kategori", related_name="article")
    title = models.CharField(max_length=64, verbose_name="Başlık")
    image = models.ImageField(blank=True, null=True, verbose_name="Görsel")
    content = RichTextField(verbose_name="İçerik")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_date']

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="Makale",related_name="comments")
    author = models.CharField(validators=[MinLengthValidator(5)], max_length=32, verbose_name="Yazar")
    content = models.TextField(validators=[MinLengthValidator(8)], max_length=512,verbose_name="Yorum")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    def __str__(self):
        return self.author
    class Meta:
        ordering = ['-created_date']
