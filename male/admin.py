from django.contrib import admin
from common import admin as base_admin
from male import models

admin.site.register(models.MaleHomePageSeo, base_admin.BaseHomePageSeoAdmin)
admin.site.register(models.MaleHomeSlider, base_admin.BaseHomeSliderAdmin)
admin.site.register(models.MaleHomeDepartment, base_admin.BaseHomeDepartmentAdmin)
admin.site.register(models.MaleAboutPageSeo, base_admin.BaseAboutPageSeoAdmin)
admin.site.register(models.MaleServicesPageSeo, base_admin.BaseServicesPageSeoAdmin)
admin.site.register(models.MaleServiceItem, base_admin.BaseServiceItemAdmin)
admin.site.register(models.MaleServiceFAQ, base_admin.BaseServiceFAQAdmin)
admin.site.register(models.MaleServiceOurCases, base_admin.BaseServiceOurCasesAdmin)
admin.site.register(models.MaleHowitworksPageSeo, base_admin.BaseHowitworksPageSeoAdmin)
admin.site.register(models.MaleBeforeAfterPageSeo, base_admin.BaseBeforeAfterPageSeoAdmin)
admin.site.register(models.MaleBeforeAfterItem, base_admin.BaseBeforeAfterItemAdmin)
admin.site.register(models.MaleBlogsPageSeo, base_admin.BaseBlogsPageSeoAdmin)
admin.site.register(models.MaleBlogCategory, base_admin.BaseBlogCategoryAdmin)


class BlogCommentInline(admin.StackedInline):
    model = models.MaleBlogComment


@admin.register(models.MaleBlog)
class MaleBlogAdmin(base_admin.BaseBlogAdmin):
    inlines = (BlogCommentInline,)
