from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from parler.admin import TranslatableAdmin

from common.models import Keywords, seo_translations, GenderSelectionPageSeo
from utils.admin import OneEntityModel

admin.site.register(Keywords, TranslatableAdmin)

seo_fields = tuple(seo_translations.keys()) + ("meta_keywords",)


class BaseHomePageSeoAdmin(TranslatableAdmin, OneEntityModel):
    fieldsets = (
        (_("Page Information"), {'fields': ('about_youtube_link', 'about_image',
                                            'howitworks_youtube_link', 
                                            'howitworks_image',)}),
        (_("Popup Information"), {'fields': ('popup',)}),
        (_("Seo Information"), {'fields': seo_fields}),
    )
    filter_vertical = ('meta_keywords',)


class BaseSearchPageSeoAdmin(TranslatableAdmin, OneEntityModel):
    fieldsets = (
        (_("Popup Information"), {'fields': ('popup',)}),
        (_("Seo Information"), {'fields': seo_fields}),
    )
    filter_vertical = ('meta_keywords',)


class BaseHomeSliderAdmin(TranslatableAdmin):
    fields = ('title', 'subtitle', 'image', 'redirect_url')
    list_display = ('title',)


class BaseHomeDepartmentAdmin(TranslatableAdmin):
    fields = ('title', 'description', 'icon')
    list_display = ('title',)


class BaseAboutPageSeoAdmin(TranslatableAdmin, OneEntityModel):
    fieldsets = (
        (_("Section 1"), {'fields': (
            'section_1_pretitle', 'section_1_title', 'section_1_subtitle', 
            'section_1_body', 'section_1_image','section_1_youtube_link')}),
        (_("Banner Information"), {'fields': ('banner_title', 'banner_description', 'banner_image')}),
        (_("Popup Information"), {'fields': ('popup',)}),
        (_("Seo Information"), {'fields': seo_fields}),
    )
    filter_vertical = ('meta_keywords',)


class BaseServicesPageSeoAdmin(TranslatableAdmin, OneEntityModel):
    fieldsets = (
        (_("Banner Information"), {'fields': ('banner_title', 'banner_description', 'banner_image')}),
        (_("Popup Information"), {'fields': ('popup',)}),
        (_("Seo Information"), {'fields': seo_fields}),
    )
    filter_vertical = ('meta_keywords',)


class BaseServiceCategoryAdmin(TranslatableAdmin):
    fieldsets = (
        (_("Content"), {'fields': (
            'title', 'slug', 'description', 'image', 'in_navbar', 'in_home', 'icon', 'order')}),
        (_("Banner Information"), {'fields': ('banner_description', 'banner_image')}),
        (_("Popup Information"), {'fields': ('popup',)}),
        (_("Seo Information"), {'fields': seo_fields}),
    )
    filter_vertical = ('meta_keywords',)
    list_display = ('title', 'slug', 'in_navbar', 'in_home', 'order')
    list_filter = ('in_navbar', 'in_home')
    list_editable = ('in_navbar', 'in_home', 'order')

    def get_prepopulated_fields(self, request, obj=None):
        return {
            'slug': ('title',),
        }


class BaseServiceItemAdmin(TranslatableAdmin):
    fieldsets = (
        (_("Content"), {'fields': ('category', 'title', 'slug', 'home_description',
                                   'content', 'image', 'in_home', 'order')}),
        (_("Banner Information"), {'fields': ('banner_description', 'banner_image')}),
        (_("Popup Information"), {'fields': ('popup',)}),
        (_("Seo Information"), {'fields': seo_fields}),
    )
    filter_vertical = ('meta_keywords',)
    list_display = ('title', 'slug', 'in_home', 'order')
    list_filter = ('in_home',)
    list_editable = ('in_home', 'order')

    def get_prepopulated_fields(self, request, obj=None):
        return {
            'slug': ('title',),
        }


class BaseServiceFAQAdmin(TranslatableAdmin):
    fields = ('service', 'question', 'answer')
    list_display = ('service', 'question', 'answer')


class BaseServiceOurCasesAdmin(TranslatableAdmin):
    fields = ('service', 'title', 'subtitle', 'description', 'image')
    list_display = ('service', 'title')


class BaseHowitworksPageSeoAdmin(TranslatableAdmin, OneEntityModel):
    fieldsets = (
        (_("Banner Information"), {'fields': ('banner_title', 'banner_description', 'banner_image')}),
        (_("Popup Information"), {'fields': ('popup',)}),
        (_("Seo Information"), {'fields': seo_fields}),
    )
    filter_vertical = ('meta_keywords',)


class BaseBeforeAfterPageSeoAdmin(TranslatableAdmin, OneEntityModel):
    fieldsets = (
        (_("Banner Information"), {'fields': ('banner_title', 'banner_description', 'banner_image')}),
        (_("Popup Information"), {'fields': ('popup',)}),
        (_("Seo Information"), {'fields': seo_fields}),
    )
    filter_vertical = ('meta_keywords',)


class BaseBeforeAfterCategoryAdmin(TranslatableAdmin):
    fieldsets = (
        (_("Content"), {'fields': (
            'title', 'slug', 'description', 'image', 'in_navbar', 'order')}),
        (_("Banner Information"), {'fields': ('banner_description', 'banner_image')}),
        (_("Popup Information"), {'fields': ('popup',)}),
        (_("Seo Information"), {'fields': seo_fields}),
    )
    filter_vertical = ('meta_keywords',)
    list_display = ('title', 'slug', 'in_navbar', 'order')
    list_filter = ('in_navbar',)
    list_editable = ('in_navbar', 'order')

    def get_prepopulated_fields(self, request, obj=None):
        return {
            'slug': ('title',),
        }


class BaseBeforeAfterItemAdmin(admin.ModelAdmin):
    fields = ('image', 'video', 'category', 'in_home')
    list_display = ('id', 'category', 'in_home')
    list_editable = ('category', 'in_home')
    list_filter = ('category', 'in_home')


class BaseBlogsPageSeoAdmin(TranslatableAdmin, OneEntityModel):
    fieldsets = (
        (_("Banner Information"), {'fields': ('banner_title', 'banner_description', 'banner_image')}),
        (_("Popup Information"), {'fields': ('popup',)}),
        (_("Seo Information"), {'fields': seo_fields}),
    )
    filter_vertical = ('meta_keywords',)


class BaseBlogCategoryAdmin(TranslatableAdmin):
    fields = ('title', 'slug', 'order')
    list_editable = ('order',)
    list_display = ('title', 'slug', 'order')

    def get_prepopulated_fields(self, request, obj=None):
        return {
            'slug': ('title',),
        }


class BaseBlogAdmin(TranslatableAdmin):
    fieldsets = (
        (_("Content Information"), {'fields': ('category', 'title', 'slug', 'description', 'content', 'image')}),
        (_("Banner Information"), {'fields': ('_banner_title', 'banner_description', 'banner_image')}),
        (_("Popup Information"), {'fields': ('popup',)}),
        (_("Seo Information"), {'fields': seo_fields}),
    )
    list_display = ('title', 'slug', 'category', 'view_count')
    list_filter = ('category',)
    search_fields = ('title', 'slug', 'description')

    def get_prepopulated_fields(self, request, obj=None):
        return {
            'slug': ('title',),
        }


class BaseContactPageSeoAdmin(TranslatableAdmin, OneEntityModel):
    fieldsets = (
        (_("Banner Information"), {'fields': ('banner_title', 'banner_description', 'banner_image')}),
        (_("Popup Information"), {'fields': ('popup',)}),
        (_("Seo Information"), {'fields': seo_fields}),
    )
    filter_vertical = ('meta_keywords',)


class BaseKVKKPageSeoAdmin(TranslatableAdmin, OneEntityModel):
    fieldsets = (
        (_("KVKK Information"), {'fields': ('content',)}),
        (_("Banner Information"), {'fields': ('banner_title', 'banner_description', 'banner_image')}),
        (_("Popup Information"), {'fields': ('popup',)}),
        (_("Seo Information"), {'fields': seo_fields}),
    )
    filter_vertical = ('meta_keywords',)


@admin.register(GenderSelectionPageSeo)
class GenderSelectionPageSeoAdmin(TranslatableAdmin, OneEntityModel):
    fieldsets = (
        (_("Popup Information"), {'fields': ('popup',)}),
        (_("Seo Information"), {'fields': seo_fields}),
    )
    filter_vertical = ('meta_keywords',)
