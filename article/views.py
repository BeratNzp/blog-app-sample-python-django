from django.shortcuts import render,get_object_or_404,redirect,reverse
from .forms import AddCommentForm
from django.contrib import messages

# Create your views here.

from .models import Article,Comment
from pages.views import getSidebarDefinitions,getAllArticles,context

def allArticles(request):
    getSidebarDefinitions(request)      #for sidebar
    context["pageTitle"] = "Anasayfa"
    getAllArticles(request)
    return render(request, 'pages/index.html', context=context)

def showArticle(request,id):
    getSidebarDefinitions(request)  # for sidebar
    article = get_object_or_404(Article,id=id)
    context["article"] = article
    context["pageTitle"] = article.title

    comments = article.comments.all()
    context["comments"] = comments

    addCommentForm = AddCommentForm()
    context["addCommentForm"] = addCommentForm

    return render(request,"pages/blog.html", context=context)

def addComment(request, id):
    article = get_object_or_404(Article,id=id)
    form = AddCommentForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        author = request.POST.get("author")
        content = request.POST.get("content")
        newComment = Comment(author=author, content=content)
        newComment.article = article
        newComment.save()
        messages.success(request, "Yorum eklendi !")
    else:
        messages.warning(request, "Hata ! Yorum eklenemedi. Daha sonra tekrar deneyebilirsiniz.")
        context["addCommentForm"] = form
    return redirect(reverse("showArticle", kwargs={"id": id}))