from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('name', 'view_html', 'body_html', 'title_service', 'description_service', 'keywords_service')


@register(Article)
class ArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'html', 'author', 'description_blog_single', 'keywords_blog_single')


@register(DataContact)
class DataContactTranslationOptions(TranslationOptions):
    fields = ('address', 'schedule_date')


@register(ArticleTeg)
class ArticleTegTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(PortfolioProject)
class PortfolioProjectTranslationOptions(TranslationOptions):
    fields = ('name', 'client', 'description')


@register(CategoriesProject)
class CategoriesProjectTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(CategoryArticle)
class CategoryArticleTranslationOptions(TranslationOptions):
    fields = ('name',)
