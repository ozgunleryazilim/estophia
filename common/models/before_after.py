from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatableModel
from parler.utils.context import switch_language

from common.models import seo_translations, SEOStarterModel
from utils.models import TimestampStarterModel


class BaseBeforeAfterPageSeo(TranslatableModel, SEOStarterModel):
    gender = ""
    translations = dict(
        banner_title=models.CharField(max_length=200, blank=True, null=True, verbose_name=_("Banner Title")),
        banner_description=RichTextField(verbose_name=_("Banner Description"), blank=True, null=True),
        **seo_translations
    )
    banner_image = models.ImageField(verbose_name=_("Banner Image"), upload_to=f"beforeafter/{gender}/banner",
                                     blank=True, null=True)

    class Meta:
        verbose_name = _("Before After Page SEO")
        verbose_name_plural = _("Before After Page SEO")
        abstract = True

    def __str__(self):
        return self.banner_title


class BaseBeforeAfterCategory(TranslatableModel, SEOStarterModel, TimestampStarterModel):
    gender = ""
    translations = dict(
        title=models.CharField(_("Başlık"), max_length=100),
        slug=models.SlugField(_("URL Uzantısı"), max_length=100),
        description=RichTextField(verbose_name=_("Açıklama"), blank=True, null=True),
        banner_description=RichTextField(_("Banner Description"), blank=True, null=True),
        **seo_translations
    )
    in_navbar = models.BooleanField(default=False, verbose_name=_("Navigasyon içerisinde mi?"))
    order = models.IntegerField(default=0, verbose_name=_("Sıralama"))
    banner_image = models.ImageField(verbose_name=_("Banner Görseli"), upload_to="before_after/category/banner",
                                     blank=True, null=True)
    image = models.ImageField(verbose_name=_("Kategori Görseli"), upload_to="before_after/category", blank=True,
                              null=True)

    def __str__(self):
        return self.title

    @property
    def banner_title(self):
        return self.title

    class Meta:
        verbose_name = _("Before After Category")
        verbose_name_plural = _("Before After Categories")
        abstract = True

    def get_absolute_url(self):
        with switch_language(self):
            return "{}?category={}".format(reverse(f'{self.gender}:before_after'), self.slug)


class BaseBeforeAfterItem(TimestampStarterModel):
    gender = ""

    image = models.ImageField(_("Service Image"), upload_to=f"beforeafter/{gender}", blank=True, null=True)
    video = models.FileField(_("Service Video"), upload_to=f"beforeafter/{gender}/videos", blank=True, null=True)
    in_home = models.BooleanField(default=False, verbose_name=_("Navigasyon içerisinde mi?"))

    class Meta:
        verbose_name = _("Before After Item")
        verbose_name_plural = _("Before After Items")
        abstract = True
