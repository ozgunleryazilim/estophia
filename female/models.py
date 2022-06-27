from django.db import models
from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatedFields

from common import models as base_models


class FemaleHomePageSeo(base_models.BaseHomePageSeo):
    translations = TranslatedFields(
        **base_models.BaseHomePageSeo.translations
    )


class FemaleHomeSlider(base_models.BaseHomeSlider):
    gender = "female"
    translations = TranslatedFields(
        **base_models.BaseHomeSlider.translations
    )


class FemaleHomeDepartment(base_models.BaseHomeDepartment):
    gender = "female"
    translations = TranslatedFields(
        **base_models.BaseHomeDepartment.translations
    )


class FemaleAboutPageSeo(base_models.BaseAboutPageSeo):
    gender = "female"
    translations = TranslatedFields(
        **base_models.BaseAboutPageSeo.translations
    )


class FemaleServicesPageSeo(base_models.BaseServicesPageSeo):
    gender = "female"
    translations = TranslatedFields(
        **base_models.BaseServicesPageSeo.translations
    )


class FemaleServiceItem(base_models.BaseServiceItem):
    gender = "female"
    translations = TranslatedFields(
        **base_models.BaseServiceItem.translations
    )

    @property
    def faq_list(self):
        return self.femaleservicefaq_set.all()

    @property
    def ourcases_list(self):
        return self.femaleserviceourcases_set.all()


class FemaleServiceFAQ(base_models.BaseServiceFAQ):
    gender = "female"
    translations = TranslatedFields(
        **base_models.BaseServiceFAQ.translations
    )
    service = models.ForeignKey(FemaleServiceItem, verbose_name=_("Related Service"), blank=True, null=True,
                                on_delete=models.CASCADE)


class FemaleServiceOurCases(base_models.BaseServiceOurCases):
    gender = "female"
    translations = TranslatedFields(
        **base_models.BaseServiceOurCases.translations
    )
    service = models.ForeignKey(FemaleServiceItem, verbose_name=_("Related Service"), blank=True, null=True,
                                on_delete=models.CASCADE)


class FemaleHowitworksPageSeo(base_models.BaseHowitworksPageSeo):
    gender = "female"
    translations = TranslatedFields(
        **base_models.BaseHowitworksPageSeo.translations
    )


class FemaleBeforeAfterPageSeo(base_models.BaseBeforeAfterPageSeo):
    gender = "female"
    translations = TranslatedFields(
        **base_models.BaseBeforeAfterPageSeo.translations
    )


class FemaleBeforeAfterItem(base_models.BaseBeforeAfterItem):
    gender = "female"


class FemaleBlogsPageSeo(base_models.BaseBlogsPageSeo):
    gender = "female"
    translations = TranslatedFields(
        **base_models.BaseBlogsPageSeo.translations
    )


class FemaleBlogCategory(base_models.BaseBlogCategory):
    gender = "female"
    translations = TranslatedFields(
        **base_models.BaseBlogCategory.translations
    )

    @property
    def blogs(self):
        return self.femaleblog_set.all()

    @property
    def blog_counts(self):
        return self.blogs.count()


class FemaleBlog(base_models.BaseBlog):
    gender = "female"
    translations = TranslatedFields(
        **base_models.BaseBlog.translations
    )
    category = models.ForeignKey(FemaleBlogCategory, blank=True, null=True, on_delete=models.SET_NULL,
                                 verbose_name=_("Category"))

    @property
    def comments(self):
        return self.femaleblogcomment_set.all()


class FemaleBlogComment(base_models.BaseBlogComment):
    gender = "female"
    blog = models.ForeignKey(FemaleBlog, verbose_name=_("Blog"), on_delete=models.CASCADE)


class FemaleContactPageSeo(base_models.BaseContactPageSeo):
    gender = "female"
    translations = TranslatedFields(
        **base_models.BaseContactPageSeo.translations
    )


class FemaleKVKKPageSeo(base_models.BaseKVKKPageSeo):
    gender = "female"
    translations = TranslatedFields(
        **base_models.BaseKVKKPageSeo.translations
    )
