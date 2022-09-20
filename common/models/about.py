from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext as _tr
from parler.models import TranslatableModel

from common.models import seo_translations, SEOStarterModel
from popup.models import Popup


class BaseAboutPageSeo(TranslatableModel, SEOStarterModel):
    gender = ""
    translations = dict(
        banner_title=models.CharField(max_length=200, blank=True, null=True, verbose_name=_("Banner Title")),
        banner_description=RichTextField(verbose_name=_("Banner Description"), blank=True, null=True),
        section_1_pretitle=models.CharField(max_length=200, default="About Us", verbose_name=_("Section 1 Main Title")),
        section_1_title=models.CharField(max_length=200, default="Welcome To<br><span>Estophia</span>",
                                         verbose_name=_("Section 1 Title")),
        section_1_subtitle=models.CharField(max_length=200, blank=True, null=True,
                                            verbose_name=_("Section 1 Subtitle")),
        section_1_body=RichTextField(verbose_name=_("Section 1 Body"), blank=True, null=True),
        **seo_translations
    )
    banner_image = models.ImageField(verbose_name=_("Banner Image"), upload_to="about/{gender}", blank=True,
                                     null=True)
    section_1_image = models.ImageField(verbose_name=_("Section 1 Image"), upload_to=f"about/{gender}", blank=True,
                                        null=True)
    section_1_youtube_link = models.URLField(verbose_name=_("Section 1 Youtube Link"), blank=True, null=True)
    popup = models.ForeignKey(Popup, on_delete=models.SET_NULL, blank=True,
                              null=True, verbose_name=_("Popup"))

    class Meta:
        verbose_name = _("About SEO")
        verbose_name_plural = _("About SEO")
        abstract = True

    def __str__(self):
        return _tr("About Page Seo")
