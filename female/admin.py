from django.contrib import admin
from common import admin as base_admin
from female import models

admin.site.register(models.FemaleHomePageSeo, base_admin.BaseHomePageSeoAdmin)
admin.site.register(models.FemaleHomeSlider, base_admin.BaseHomeSliderAdmin)
admin.site.register(models.FemaleHomeDepartment, base_admin.BaseHomeDepartmentAdmin)
admin.site.register(models.FemaleAboutPageSeo, base_admin.BaseAboutPageSeoAdmin)
admin.site.register(models.FemaleServicesPageSeo, base_admin.BaseServicesPageSeoAdmin)
admin.site.register(models.FemaleServiceCategory, base_admin.BaseServiceCategoryAdmin)
admin.site.register(models.FemaleServiceItem, base_admin.BaseServiceItemAdmin)
admin.site.register(models.FemaleServiceFAQ, base_admin.BaseServiceFAQAdmin)
admin.site.register(models.FemaleServiceOurCases, base_admin.BaseServiceOurCasesAdmin)
admin.site.register(models.FemaleHowitworksPageSeo, base_admin.BaseHowitworksPageSeoAdmin)
admin.site.register(models.FemaleBeforeAfterPageSeo, base_admin.BaseBeforeAfterPageSeoAdmin)
admin.site.register(models.FemaleBeforeAfterCategory, base_admin.BaseBeforeAfterCategoryAdmin)
admin.site.register(models.FemaleBeforeAfterItem, base_admin.BaseBeforeAfterItemAdmin)
admin.site.register(models.FemaleBlogsPageSeo, base_admin.BaseBlogsPageSeoAdmin)
admin.site.register(models.FemaleBlogCategory, base_admin.BaseBlogCategoryAdmin)
admin.site.register(models.FemaleContactPageSeo, base_admin.BaseContactPageSeoAdmin)
admin.site.register(models.FemaleKVKKPageSeo, base_admin.BaseKVKKPageSeoAdmin)
admin.site.register(models.FemaleSearchPageSeo, base_admin.BaseSearchPageSeoAdmin)


class BlogCommentInline(admin.StackedInline):
    model = models.FemaleBlogComment


@admin.register(models.FemaleBlog)
class FemaleBlogAdmin(base_admin.BaseBlogAdmin):
    inlines = (BlogCommentInline,)
