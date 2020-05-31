from django.shortcuts import render
from article.models import Article,Category
import random

# Create your views here.
context = {}
itemLimit1 = 5

def getArticlesCount(request):
    allArticlesCount = Article.objects.count()
    context["allArticlesCount"] = allArticlesCount

def getAllArticles(request):
    getAllArticles = Article.objects.all()
    if "category" in context:
        del context["category"]
    context["articles"] = getAllArticles

def getLimitedArticles(request):
    getLimitedArticles = Article.objects.all()[:itemLimit1]
    context["articles"] = getLimitedArticles

def getRandomArticles(request):
    if Article.objects.count() >= itemLimit1:
        randomArticles = random.sample(list(Article.objects.all()), itemLimit1)
    else:
        randomArticles = random.sample(list(Article.objects.all()), Article.objects.count())
    context["randomArticles"] = randomArticles

def getAllCategories(request):
    categories = Category.objects.all()
    #context["categories"] = categories
    categoryList = {}
    for category in categories:
        articles = Article.objects.filter(category=category)
        counter = 0
        for article in articles:
            counter += 1
        categoryList[category.title] = counter
    context["categoryList"]=categoryList


def getSidebarDefinitions(request):
    getRandomArticles(request)
    getAllCategories(request)
    getArticlesCount(request)

def index(request):
    context["pageTitle"] = "Anasayfa"

    getSidebarDefinitions(request)      #for sidebar

    if request.GET.get("category"):
        categoryFilter = request.GET.get("category")
        context["category"] = categoryFilter
        if "keywords" in context:
            del context["keywords"]
        articles = Article.objects.filter(category__title=categoryFilter)
        context["articles"] = articles
    elif "category" in context and not request.GET.get("category"):
        del context["category"]
        getLimitedArticles(request)


    elif request.GET.get("keywords"):
        keywordsFilter = request.GET.get("keywords")
        articles = Article.objects.filter(title__contains = keywordsFilter)
        if "category" in context:
            del context["category"]
        context["articles"] = articles
        context["keywords"] = keywordsFilter
    elif "keywords" in context and not request.GET.get("keywords"):
        del context["keywords"]
        getLimitedArticles(request)

    else:
        if "keywords" in context:
            del context["keywords"]
        if "category" in context:
            del context["category"]
        getLimitedArticles(request)
    return render(request, "pages/index.html", context=context)

def about(request):
    getSidebarDefinitions(request)  # for sidebar
    context["pageTitle"] = "Hakkımda"
    return render(request, 'pages/about.html', context=context)

def contact(request):
    getSidebarDefinitions(request)  # for sidebar
    context["pageTitle"] = "İletişim"
    return render(request, 'pages/contact.html', context=context)
