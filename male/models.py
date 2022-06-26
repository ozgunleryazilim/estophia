from django.db import models
from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatedFields

from common import models as base_models


class MaleHomePageSeo(base_models.BaseHomePageSeo):
    translations = TranslatedFields(
        **base_models.BaseHomePageSeo.translations
    )


class MaleHomeSlider(base_models.BaseHomeSlider):
    gender = "male"
    translations = TranslatedFields(
        **base_models.BaseHomeSlider.translations
    )


class MaleHomeDepartment(base_models.BaseHomeDepartment):
    gender = "male"
    translations = TranslatedFields(
        **base_models.BaseHomeDepartment.translations
    )


class MaleAboutPageSeo(base_models.BaseAboutPageSeo):
    gender = "male"
    translations = TranslatedFields(
        **base_models.BaseAboutPageSeo.translations
    )


class MaleServicesPageSeo(base_models.BaseServicesPageSeo):
    gender = "male"
    translations = TranslatedFields(
        **base_models.BaseServicesPageSeo.translations
    )


class MaleServiceItem(base_models.BaseServiceItem):
    gender = "male"
    translations = TranslatedFields(
        **base_models.BaseServiceItem.translations
    )

    @property
    def faq_list(self):
        return self.maleservicefaq_set.all()

    @property
    def ourcases_list(self):
        return self.maleserviceourcases_set.all()


class MaleServiceFAQ(base_models.BaseServiceFAQ):
    gender = "male"
    translations = TranslatedFields(
        **base_models.BaseServiceFAQ.translations
    )
    service = models.ForeignKey(MaleServiceItem, verbose_name=_("Related Service"), blank=True, null=True,
                                on_delete=models.CASCADE)


class MaleServiceOurCases(base_models.BaseServiceOurCases):
    gender = "male"
    translations = TranslatedFields(
        **base_models.BaseServiceOurCases.translations
    )
    service = models.ForeignKey(MaleServiceItem, verbose_name=_("Related Service"), blank=True, null=True,
                                on_delete=models.CASCADE)


class MaleHowitworksPageSeo(base_models.BaseHowitworksPageSeo):
    gender = "male"
    translations = TranslatedFields(
        **base_models.BaseHowitworksPageSeo.translations
    )


class MaleBeforeAfterPageSeo(base_models.BaseBeforeAfterPageSeo):
    gender = "male"
    translations = TranslatedFields(
        **base_models.BaseBeforeAfterPageSeo.translations
    )


class MaleBeforeAfterItem(base_models.BaseBeforeAfterItem):
    gender = "male"


class MaleBlogsPageSeo(base_models.BaseBlogsPageSeo):
    gender = "male"
    translations = TranslatedFields(
        **base_models.BaseBlogsPageSeo.translations
    )


class MaleBlogCategory(base_models.BaseBlogCategory):
    gender = "male"
    translations = TranslatedFields(
        **base_models.BaseBlogCategory.translations
    )

    @property
    def blogs(self):
        return self.maleblog_set.all()

    @property
    def blog_counts(self):
        return self.blogs.count()


class MaleBlog(base_models.BaseBlog):
    gender = "male"
    translations = TranslatedFields(
        **base_models.BaseBlog.translations
    )
    category = models.ForeignKey(MaleBlogCategory, blank=True, null=True, on_delete=models.SET_NULL,
                                 verbose_name=_("Category"))

    @property
    def comments(self):
        return self.maleblogcomment_set.all()


class MaleBlogComment(base_models.BaseBlogComment):
    gender = "female"
    blog = models.ForeignKey(MaleBlog, verbose_name=_("Blog"), on_delete=models.CASCADE)
