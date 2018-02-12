from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.
class Articleenglish(models.Model):
    article_title = models.CharField(max_length=200)
    article_text = models.TextField()
    article_date = models.DateField()
    article_likes = models.IntegerField(default=0)
    article_image = models.ImageField(null=True, blank=True, upload_to="images/",
                                      verbose_name=u'картинка', )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.article_title

class Videotrailer(models.Model):
    trailer_title = models.CharField(max_length=200, blank=True, null=True, default=None)
    trailer_text = models.TextField(blank=True, null=True, default=None)
    trailer_image = models.ImageField(null=True, blank=True, upload_to="images/",
                                      verbose_name=u'картинка', )
    trailer_video = EmbedVideoField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.trailer_title

class Videokritika(models.Model):
    kritika_title = models.CharField(max_length=200, blank=True, null=True, default=None)
    kritika_text = models.TextField(blank=True, null=True, default=None)
    kritika_image = models.ImageField(null=True, blank=True, upload_to="images/",
                                      verbose_name=u'картинка', )
    kritika_video = EmbedVideoField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.kritika_title

