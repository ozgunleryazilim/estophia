from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields

from common.models import seo_translations, SEOStarterModel


class BaseHomePageSeo(TranslatableModel, SEOStarterModel):
    translations = dict(
        **seo_translations
    )

    class Meta:
        verbose_name = _("Home SEO")
        verbose_name_plural = _("Home SEO")
        abstract = True


class BaseHomeSlider(TranslatableModel):
    gender = ""

    translations = dict(
        title=models.CharField(max_length=200, verbose_name=_("Title")),
        subtitle=models.CharField(max_length=200, verbose_name=_("Subtitle"), blank=True, null=True)
    )
    image = models.ImageField(verbose_name=_("Slider Image"), upload_to=f"home/slider/{gender}/")

    class Meta:
        verbose_name = _("Home Slider")
        verbose_name_plural = _("Home Sliders")
        abstract = True


class BaseHomeDepartment(TranslatableModel):
    gender = ""

    translations = dict(
        title=models.CharField(max_length=200, verbose_name=_("Title")),
        description=models.CharField(max_length=200, verbose_name=_("Description"), blank=True, null=True)
    )
    icon = models.ImageField(verbose_name=_("Icon"), upload_to=f"home/icons/{gender}/", blank=True, null=True)

    class Meta:
        verbose_name = _("Home Department")
        verbose_name_plural = _("Home Departments")
        abstract = True
