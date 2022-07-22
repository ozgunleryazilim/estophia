from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext as _tr
from parler.models import TranslatableModel
from parler.utils.context import switch_language

from common.models import seo_translations, SEOStarterModel
from utils.models import TimestampStarterModel


class BaseBlogsPageSeo(TranslatableModel, SEOStarterModel):
    gender = ""
    translations = dict(
        banner_title=models.CharField(max_length=200, blank=True, null=True, verbose_name=_("Banner Title")),
        banner_description=RichTextField(verbose_name=_("Banner Description"), blank=True, null=True),
        **seo_translations
    )
    banner_image = models.ImageField(verbose_name=_("Banner Image"), upload_to=f"blogs/{gender}/banner", blank=True,
                                     null=True)

    class Meta:
        verbose_name = _("Blogs Page SEO")
        verbose_name_plural = _("Blogs Page SEO")
        abstract = True

    def __str__(self):
        return _tr("Blog Page Seo")


class BaseBlogCategory(TranslatableModel, TimestampStarterModel):
    gender = ""
    translations = dict(
        title=models.CharField(_("Title"), max_length=200),
        slug=models.SlugField(_("Slug"), max_length=200),
    )
    order = models.IntegerField(default=1, verbose_name=_("Ordering"))

    class Meta:
        verbose_name = _("Blog Category")
        verbose_name_plural = _("Blog Categories")
        abstract = True

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        with switch_language(self):
            return "%s?category=%s" % (reverse(f'{self.gender}:blog_list'), self.slug)


class BaseBlog(TranslatableModel, SEOStarterModel, TimestampStarterModel):
    gender = ""
    category = None
    translations = dict(
        title=models.CharField(_("Title"), max_length=200),
        description=models.TextField(_("Title"), max_length=200, blank=True, null=True),
        slug=models.SlugField(_("Slug"), max_length=200),
        content=RichTextUploadingField(_("Content Body 1"), blank=True, null=True),
        _banner_title=models.CharField(_("Banner Title"), max_length=200, blank=True, null=True),
        banner_description=RichTextField(verbose_name=_("Banner Description"), blank=True, null=True),
        **seo_translations
    )
    image = models.ImageField(verbose_name=_("Image"), upload_to="blogs", blank=True, null=True)
    banner_image = models.ImageField(verbose_name=_("Banner Image"), upload_to="blogs/banner", blank=True, null=True)
    view_count = models.IntegerField(default=0, verbose_name=_("View Count"))

    class Meta:
        verbose_name = _("Blog")
        verbose_name_plural = _("Blogs")
        abstract = True

    def __str__(self):
        return self.title

    @property
    def banner_title(self):
        return self._banner_title or self.title

    def increase_view_count(self):
        self.view_count += 1
        self.save()

    def get_absolute_url(self):
        with switch_language(self):
            return reverse(f'{self.gender}:blog_detail', args=(self.slug,))

    def save(self, *args, **kwargs):
        if not self._banner_title:
            self._banner_title = self.title
        if not self.seo_title:
            self.seo_title = self.title
        super().save(*args, **kwargs)


class BaseBlogComment(TimestampStarterModel):
    blog = None
    name = models.CharField(verbose_name=_("Name *"), max_length=200)
    email = models.EmailField(verbose_name=_("Email *"))
    comment = models.TextField(verbose_name=_("Write review *"))
    is_approved = models.BooleanField(verbose_name=_("Is Approved"), default=False)

    class Meta:
        verbose_name = _("Blog Comment")
        verbose_name_plural = _("Blog Comments")
        ordering = ('-created_date',)
        abstract = True
