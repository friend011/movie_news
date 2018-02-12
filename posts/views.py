from django.shortcuts import render
#from .forms import UserForm
from .models import *

# Create your views here.


def index(request):
    articleenglishs  = Articleenglish.objects.filter(is_active=True)
    videotrailers  = Videotrailer.objects.filter(is_active=True)
    videokritiks  = Videokritika.objects.filter(is_active=True)

    return render(request, "posts/index.html", locals())

def article_englishs(request):
    articleenglishs  = Articleenglish.objects.filter(is_active=True)

    return render(request, "posts/articles.html", locals())

def article_english(request, articleenglish_id):
    articleenglish = Articleenglish.objects.get(id=articleenglish_id)

    return render(request, 'posts/article.html', locals())

def video_trailers(request):
    videotrailers  = Videotrailer.objects.filter(is_active=True)

    return render(request, "posts/video_trailers.html", locals())

def video_trailer(request, videotrailer_id):
    videotrailer = Videotrailer.objects.get(id=videotrailer_id)

    return render(request, 'posts/video_trailer.html', locals())

def video_kritiks(request):
    videokritiks  = Videokritika.objects.filter(is_active=True)

    return render(request, "posts/video_kritiks.html", locals())

def video_kritik(request, videokritik_id):
    videokritik = Videokritika.objects.get(id=videokritik_id)

    return render(request, 'posts/video_kritik.html', locals())


# def product(request, product_id):
#     product = Product.objects.get(id=product_id)
#     return render(request, 'products/product.html', locals())

"""
def article(request):
    args = {}

    args['article'] = Article.objects.get(id=article_id)

    return render(request, 'posts/article.html', locals())
"""