from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext as _tr
from parler.models import TranslatableModel, TranslatedFields

from common.models import seo_translations, SEOStarterModel
from popup.models import Popup


class GenderSelectionPageSeo(TranslatableModel, SEOStarterModel):
    translations = TranslatedFields(
        **seo_translations
    )
    popup = models.ForeignKey(Popup, on_delete=models.SET_NULL, blank=True,
                              null=True, verbose_name=_("Popup"))

    class Meta:
        verbose_name = _("Gender Selection Page SEO")
        verbose_name_plural = _("Gender Selection Page SEO")

    def __str__(self):
        return _tr("Gender Selection Page SEO")
