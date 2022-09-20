from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext as _tr
from parler.models import TranslatableModel

from common.models import seo_translations, SEOStarterModel
from popup.models import Popup


class BaseContactPageSeo(TranslatableModel, SEOStarterModel):
    gender = ""
    translations = dict(
        banner_title=models.CharField(max_length=200, blank=True, null=True, verbose_name=_("Banner Title")),
        banner_description=RichTextField(verbose_name=_("Banner Description"), blank=True, null=True),
        **seo_translations
    )
    banner_image = models.ImageField(verbose_name=_("Banner Image"), upload_to=f"contact/{gender}", blank=True,
                                     null=True)
    popup = models.ForeignKey(Popup, on_delete=models.SET_NULL, blank=True,
                              null=True, verbose_name=_("Popup"))

    class Meta:
        verbose_name = _("Contact Page SEO")
        verbose_name_plural = _("Contact Page SEO")
        abstract = True

    def __str__(self):
        return _tr("Contact Page Seo")
