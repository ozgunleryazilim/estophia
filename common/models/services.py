from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatableModel
from parler.utils.context import switch_language

from common.models import seo_translations, SEOStarterModel
from utils.models import TimestampStarterModel


class BaseServicesPageSeo(TranslatableModel, SEOStarterModel):
    gender = ""
    translations = dict(
        banner_title=models.CharField(max_length=200, blank=True, null=True, verbose_name=_("Banner Title")),
        banner_description=RichTextField(verbose_name=_("Banner Description"), blank=True, null=True),
        **seo_translations
    )
    banner_image = models.ImageField(verbose_name=_("Banner Image"), upload_to="about/{gender}", blank=True,
                                     null=True)

    class Meta:
        verbose_name = _("Services SEO")
        verbose_name_plural = _("Services SEO")
        abstract = True

    def __str__(self):
        return self.banner_title


class BaseServiceItem(TranslatableModel, SEOStarterModel, TimestampStarterModel):
    gender = ""
    translations = dict(
        title=models.CharField(_("Title"), max_length=200),
        banner_description=RichTextField(_("Banner Description"), blank=True, null=True),
        home_description=RichTextField(_("Home Description"), blank=True, null=True),
        slug=models.SlugField(_("Slug"), max_length=200),
        content=RichTextUploadingField(_("Content Body"), blank=True, null=True),
        **seo_translations
    )
    banner_image = models.ImageField(_("Banner Image"), upload_to="services/banner", blank=True, null=True)
    image = models.ImageField(_("Service Image"), upload_to="services", blank=True, null=True)
    in_home = models.BooleanField(_("In home page services section?"), default=False)
    order = models.IntegerField(default=1, verbose_name=_("Ordering"))

    class Meta:
        verbose_name = _("Service Item")
        verbose_name_plural = _("Service Items")
        abstract = True

    @property
    def banner_title(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        with switch_language(self):
            return reverse(f'{self.gender}:services_detail', args=(self.slug,))


class BaseServiceFAQ(TranslatableModel):
    translations = dict(
        question=models.CharField(_("Question"), max_length=200),
        answer=RichTextField(_("Answer"), blank=True, null=True),
    )

    class Meta:
        verbose_name = _("Service Frequently Asked Question")
        verbose_name_plural = _("Service Frequently Asked Questions")
        abstract = True

    def __str__(self):
        return self.question


class BaseServiceOurCases(TranslatableModel):
    gender = ""
    translations = dict(
        title=models.CharField(_("Title"), max_length=200),
        subtitle=models.CharField(_("Subtitle"), max_length=200, blank=True, null=True),
        description=RichTextField(_("Description"), blank=True, null=True),
    )
    image = models.ImageField(_("Service Image"), upload_to=f"services/{gender}/cases", blank=True, null=True)

    class Meta:
        verbose_name = _("Service Our Cases")
        verbose_name_plural = _("Service Our Cases")
        abstract = True

    def __str__(self):
        return self.title
