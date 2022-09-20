from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext as _tr
from parler.models import TranslatableModel, TranslatedFields

from common.models import seo_translations, SEOStarterModel
from popup.models import Popup


class BaseHomePageSeo(TranslatableModel, SEOStarterModel):
    translations = dict(
        **seo_translations
    )
    about_youtube_link = models.URLField(verbose_name=_("About Youtube Link"), blank=True, null=True)
    about_image = models.ImageField(verbose_name=_("About Section Image"), upload_to=f"home/seo", blank=True, null=True)

    howitworks_youtube_link = models.URLField(verbose_name=_("About Youtube Link"), blank=True, null=True)
    howitworks_image = models.ImageField(verbose_name=_("How it works Section Image"), upload_to=f"home/seo",
                                         blank=True, null=True)
    popup = models.ForeignKey(Popup, on_delete=models.SET_NULL, blank=True,
                              null=True, verbose_name=_("Popup"))
    class Meta:
        verbose_name = _("Home SEO")
        verbose_name_plural = _("Home SEO")
        abstract = True

    def __str__(self):
        return _tr("Home Page Seo")


class BaseHomeSlider(TranslatableModel):
    gender = ""

    translations = dict(
        title=models.CharField(max_length=200, verbose_name=_("Title")),
        subtitle=models.CharField(max_length=200, verbose_name=_("Subtitle"), blank=True, null=True),
        redirect_url=models.CharField(verbose_name=_("Redirect Link"), blank=True, null=True, max_length=500),
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
