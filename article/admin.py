from django.contrib import admin
from article.models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
	list_display = ( 'title', 'author', 'publish_time', 'update_time', 'content', 'classify', 'page_view',)

admin.site.register(Article, ArticleAdmin)	