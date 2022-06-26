from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatableModel

from common.models import seo_translations, SEOStarterModel


class BaseHowitworksPageSeo(TranslatableModel, SEOStarterModel):
    gender = ""
    translations = dict(
        banner_title=models.CharField(max_length=200, blank=True, null=True, verbose_name=_("Banner Title")),
        banner_description=RichTextField(verbose_name=_("Banner Description"), blank=True, null=True),
        **seo_translations
    )
    banner_image = models.ImageField(verbose_name=_("Banner Image"), upload_to="howitworks/{gender}", blank=True,
                                     null=True)

    class Meta:
        verbose_name = _("How It Works Page SEO")
        verbose_name_plural = _("How It Works Page SEO")
        abstract = True

    def __str__(self):
        return self.banner_title
