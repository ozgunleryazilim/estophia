from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatableModel
from django.utils.translation import ugettext as _tr

from common.models import seo_translations, SEOStarterModel


class BaseSearchPageSeo(TranslatableModel, SEOStarterModel):
    translations = dict(
        **seo_translations
    )

    class Meta:
        verbose_name = _("Search Page SEO")
        verbose_name_plural = _("Search Page SEO")
        abstract = True

    def __str__(self):
        return _tr("Search Page Seo")

