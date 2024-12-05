from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, HttpResponse
from django.utils.translation import gettext as _
from django.db.models import Count
from django.db.models import Prefetch
from .forms import *
from .models import *


def get_menu_and_services(current_menu):
    return {
        "current_menu": current_menu,
        "services": Service.objects.all().order_by('position'),
        "contacts": DataContact.objects.all(),
    }


def about(request):
    return render(
        request,
        'about.html',
        {**{
            "breadcrumbs": [
                {
                    "name": _("Головна"),
                    "link": "/"
                },
                {
                    "name": _("Про нас"),
                    "link": None}
            ]
        }, **get_menu_and_services(_('Про нас'))})


def contact(request):
    if request.method == 'POST':
        try:
            form = Contact(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return True
        except:
            return False
    return False


def main(request):
    send_consultation = contact(request)
    # Fetch all blog articles without any limit or pagination
    articles = Article.objects.all().order_by('-date')  # Fetch all articles sorted by date
    return render(request, 'index.html', {
        "category": CategoriesProject.objects.all(),
        "projects": PortfolioProject.objects.all(),
        "articles": articles,  # Pass all articles to the template
        "send_consultation": send_consultation,
        **get_menu_and_services(_('Головна'))
    })



def blog(request):
    category = request.GET.get("category")
    tag = request.GET.get("tag")
    search_text = request.GET.get("text")
    page_count = 1
    page = request.GET.get("page")

    if page:
        page_count = int(page)
    article = None
    if category:
        article = Article.objects.filter(categories=category)
    if tag:
        article = Article.objects.filter(teg=tag)
    if search_text:
        article = Article.objects.filter(Q(title__contains=search_text) | Q(description__contains=search_text))
    if article is None:
        article = Article.objects.all()
    category = CategoryArticle.objects.all()
    list_category = []
    for i in category:
        list_category.append({"obj": i, "count": len(Article.objects.filter(categories=i))})
    list_article = Paginator(article.order_by('date'), 3)
    return render(request, 'blog.html', {**{
        "article": list_article.page(page_count),
        "cur_page": page_count,
        "pages": list_article.page_range,
        "category": list_category,
        "tags": ArticleTeg.objects.all(),
        "last_articles": Article.objects.all()[:5],
        "breadcrumbs": [
            {
                "name": _("Головна"),
                "link": "/"
            },
            {
                "name": _("Блог"),
                "link": None
            }]}, **get_menu_and_services(_('Блог'))})


def single_blog(request, name):
    category = CategoryArticle.objects.all()
    list_category = []
    if request.method == "POST":
        form = Comment(request.POST)
        if form.is_valid():
            article = Article.objects.get(id=name)
            article.commentaries.add(form.save())
            article.save()
    for i in category:
        list_category.append({"obj": i, "count": len(Article.objects.filter(categories=i))})
    article = Article.objects.get(id=name)
    return render(request, 'blog-single.html', {**{
        "article": article,
        "category": list_category,
        "tags": ArticleTeg.objects.all(),
        "last_articles": Article.objects.all()[:5],
        "breadcrumbs": [
            {
                "name": _("Головна"),
                "link": "/"
            },
            {
                "name": _("Блог"),
                "link": "/blog"
            },
            {
                "name": article.title,
                "link": None
            }]}, **get_menu_and_services(_('Блог'))})


def portfolio_details(request, name):
    project = PortfolioProject.objects.prefetch_related(Prefetch('images', queryset=Image.objects.order_by('priority'))).get(id=name)
    projects = PortfolioProject.objects.filter(service=project.service.id).exclude(id=project.id).prefetch_related(Prefetch('images', queryset=Image.objects.order_by('priority')))
    unique_category_ids = CategoriesProject.objects.filter(pk__in=projects.values('category').distinct())
    return render(request, 'portfolio-details.html', {**{
        "i": project,
        "breadcrumbs": [
            {
                "name": _("Головна"),
                "link": "/"
            },
            {
                "name": _("Портфоліо"),
                "link": "/#portfolio"
            },
            {
                "name": project.name,
                "link": None
            }]}, **{
                      "category": unique_category_ids,
                      "projects": projects,
                  }, **get_menu_and_services(_('Портфоліо'))})


def services_details(request, name):
    send_consultation = consultation(request)
    services = Service.objects.get(id=name)
    projects = PortfolioProject.objects.filter(service=services.id).prefetch_related(Prefetch('images', queryset=Image.objects.order_by('priority')))
    unique_category_ids = CategoriesProject.objects.filter(pk__in=projects.values('category').distinct())
    return render(request, 'services-details.html', {**{
        "content": services,
        "send_consultation": send_consultation,
        "breadcrumbs": [
            {
                "name": _("Головна"),
                "link": "/"
            },
            {
                "name": _("Послуги"),
                "link": "/#services"
            },
            {
                "name": services.name,
                "link": None
            }]}, **{
                      "category": unique_category_ids,
                      "projects": projects,
                  }, **get_menu_and_services(_('Послуги'))})


def error_404_view(request, exception):
    return render(request, 'blocks/404.html')


def form_contact(request):
    return HttpResponse(request)


def consultation(request):
    if request.method == 'POST':
        try:
            form = Consultation_form(request.POST)
            if form.is_valid():
                form.save()
                return True
        except:
            return False
    return False


def form_consultation(request):
    return HttpResponse(request)
