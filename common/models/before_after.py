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
    banner_image = models.ImageField(verbose_name=_("Banner Image"), upload_to=f"beforeafter/{gender}/banner", blank=True,
                                     null=True)

    class Meta:
        verbose_name = _("Before After Page SEO")
        verbose_name_plural = _("Before After Page SEO")
        abstract = True

    def __str__(self):
        return self.banner_title


class BaseBeforeAfterItem(TimestampStarterModel):
    gender = ""

    image = models.ImageField(_("Service Image"), upload_to=f"beforeafter/{gender}", blank=True, null=True)
    video = models.FileField(_("Service Video"), upload_to=f"beforeafter/{gender}/videos", blank=True, null=True)

    class Meta:
        verbose_name = _("Before After Item")
        verbose_name_plural = _("Before After Items")
        abstract = True


