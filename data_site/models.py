from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Image(models.Model):
    priority = models.IntegerField(verbose_name="Пріорітет зображення")
    image = models.ImageField(verbose_name="Фото")

    def __str__(self):
        return str(self.image)

    class Meta:
        verbose_name = "Зображення"
        verbose_name_plural = "Зображення"


class CategoryArticle(models.Model):
    name = models.CharField(verbose_name="Назва", max_length=1024, null=False)

    class Meta:
        verbose_name = "Категорія статті"
        verbose_name_plural = "Категорії статей"


class ArticleTeg(models.Model):
    name = models.CharField(verbose_name="Назва", max_length=1024, null=False)

    class Meta:
        verbose_name = "Тег статті"
        verbose_name_plural = "Теги статей"


class Article(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=2048, default='', blank=True)
    description = RichTextUploadingField(verbose_name="Опис", default='', blank=True)
    date = models.DateField(verbose_name="Дата публікації", default='', blank=True)
    image = models.ImageField(verbose_name="Фото", default='', blank=True)
    html = RichTextUploadingField(verbose_name="Тіло в html", default='', blank=True)
    author = models.CharField(verbose_name="ПІБ", max_length=1024, default='', blank=True)
    categories = models.ManyToManyField(CategoryArticle, verbose_name="Катагорії", default='', blank=True)
    teg = models.ManyToManyField(ArticleTeg, verbose_name="Теги", default='', blank=True)
    description_blog_single = RichTextUploadingField(verbose_name="Опис сторінки блогу (SEO)", default='', blank=True)
    keywords_blog_single = RichTextUploadingField(verbose_name="Ключові слова сторінки блогу (SEO)", default='', blank=True)

    class Meta:
        verbose_name = "Стаття блогу"
        verbose_name_plural = "Статті блогу"


class Communication(models.Model):
    name = models.CharField(verbose_name="Ім'я", max_length=1024, default='', blank=True)
    email = models.EmailField(verbose_name="email", default='', blank=True)
    topic = models.CharField(verbose_name="Тема", max_length=2048, default='', blank=True)
    description = RichTextUploadingField(verbose_name="Опис", max_length=100000, default='', blank=True)
    file = models.FileField(upload_to='brief', default='', blank=True)

    def __str__(self):
        return str(self.name) + ' ' + str(self.email)

    class Meta:
        verbose_name = "Дані зворотнього зв'язку"
        verbose_name_plural = "Дані зворотнього зв'язку"


class Service(models.Model):
    position = models.IntegerField(null=True)
    name = models.CharField(max_length=512)
    title_service = models.CharField(verbose_name="Загаловки сторінки послуг (SEO)", max_length=2048, default='', blank=True)
    description_service = RichTextUploadingField(verbose_name="Опис сторінки послуг (SEO)", default='', blank=True)
    keywords_service = RichTextUploadingField(verbose_name="Ключові слова сторінки послуг (SEO)", default='', blank=True)
    img = models.ImageField(verbose_name="Фото", default='', blank=True)
    view_html = RichTextUploadingField(verbose_name="Шаблон в списку", default='', blank=True)
    body_html = RichTextUploadingField(verbose_name="Шаблон контенту", default='', blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Послуга"
        verbose_name_plural = "Послуги"


class CategoriesProject(models.Model):
    name = models.CharField(verbose_name="Назва", max_length=1024)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категорія проекту"
        verbose_name_plural = "Категорії проектів"


class PortfolioProject(models.Model):
    name = models.CharField(verbose_name="Назва", max_length=1024)
    date = models.DateField(verbose_name="Дата", max_length=1024)
    client = models.CharField(verbose_name="Клієнт", max_length=1024, default='', blank=True)
    url = models.URLField(verbose_name="Посилання", default='', blank=True)
    description = RichTextUploadingField(verbose_name="Опис", default='', blank=True)
    main_image = models.ImageField(verbose_name="Фото", blank=True)
    images = models.ManyToManyField(Image, verbose_name="Фото", default='', blank=True)
    category = models.ForeignKey(CategoriesProject, verbose_name="Категорія", null=False, on_delete=models.NOT_PROVIDED, default='', blank=True)
    service = models.ForeignKey(Service, verbose_name="Сервіс", null=True, on_delete=models.NOT_PROVIDED, default='', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Портфоліо"
        verbose_name_plural = "Портфоліо"


class DataContact(models.Model):
    mobile_phone = models.CharField(verbose_name="Мобільний телефон", max_length=2048)
    email = models.CharField(verbose_name="Поштова скринька", max_length=2048)
    address = models.CharField(verbose_name="Адреса офісу", max_length=2048, default='', blank=True)
    schedule_date = models.CharField(verbose_name="Дні роботи", max_length=2048, default='', blank=True)
    schedule_time = models.CharField(verbose_name="Години роботи", max_length=2048, default='', blank=True)
    telegram_link = models.CharField(verbose_name="Посилання на telegram", max_length=2048, default='', blank=True)
    facebook_link = models.CharField(verbose_name="Посилання на facebook", max_length=2048, default='', blank=True)
    linkedin_link = models.CharField(verbose_name="Посилання на linkedin", max_length=2048, default='', blank=True)
    instagram_link = models.CharField(verbose_name="Посилання на instagram", max_length=2048, default='', blank=True)

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контактні дані"


class Consultation(models.Model):
    name = models.CharField(verbose_name="Ім'я", max_length=2048)
    email = models.EmailField(verbose_name="Електронна пошта", max_length=2048)

    def __str__(self):
        return str(self.name) + ' ' + str(self.email)

    class Meta:
        verbose_name = "Консультація"
        verbose_name_plural = "Консультації"
