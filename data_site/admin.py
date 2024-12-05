from django.contrib import admin
from .models import Image, PortfolioProject, Communication, CategoriesProject, CategoryArticle, Article, ArticleTeg, \
    Service, DataContact, Consultation
from modeltranslation.admin import TranslationAdmin


class PostAdmin(TranslationAdmin):
    pass


admin.site.register(Image)
admin.site.register(PortfolioProject, PostAdmin)
admin.site.register(Communication)
admin.site.register(CategoriesProject, PostAdmin)
admin.site.register(CategoryArticle, PostAdmin)
admin.site.register(Article, PostAdmin)
admin.site.register(Consultation)
admin.site.register(ArticleTeg, PostAdmin)
admin.site.register(Service, PostAdmin)
admin.site.register(DataContact, PostAdmin)
# Register your models here.

admin.site.site_title = 'TRANSIMPEX'
admin.site.site_header = 'TRANSIMPEX'
