from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from posts import views
from .import views

# працює без views
# urlpatterns = [
#     path('', ListView.as_view(queryset=Article.objects.all().order_by("-date")[:20],
#                                    template_name="posts/posts.html")),
#     re_path(r'^(?P<pk>\d+)$', DetailView.as_view(model=Article, template_name='posts/post.html')),
# ]

urlpatterns = [

    path('articleenglishs', views.article_englishs, name='articleenglishs'),
    re_path(r'^articleenglishs/get/(?P<articleenglish_id>\d+)/$', views.article_english, name='articleenglish'),
    path('videotrailers', views.video_trailers, name='video_trailers'),
    re_path(r'^videotrailers/get/(?P<videotrailer_id>\d+)/$', views.video_trailer, name='video_trailer'),

    path('videokritiks', views.video_kritiks, name='video_kritiks'),
    re_path(r'^videokritiks/get/(?P<videokritik_id>\d+)/$', views.video_kritik, name='video_kritik'),
    
    path('', views.index, name='index'),


]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
