from django.contrib import admin
from .models import Article, Comment, Hashtag

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk','title','content','created_at','updated_at',)

# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk','content','created_at','updated_at',)

# admin.site.register(Comment, CommentAdmin) <= @admin.register(Comment)와 같은 표현임

@admin.register(Hashtag)
class HashtaAdmin(admin.ModelAdmin):
    list_display = ('content', )
