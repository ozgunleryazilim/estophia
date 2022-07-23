from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.contrib.sitemaps.views import sitemap
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView

from common.sitemaps import CommonStaticViewSitemap
from config.views import GenderSelectionPage
from female.sitemaps import (FemaleStaticViewSitemap, FemaleServiceSitemap, FemaleBlogSitemap,
                             FemaleServiceCategorySitemap)
from male.sitemaps import MaleBlogSitemap, MaleServiceSitemap, MaleStaticViewSitemap, MaleServiceCategorySitemap

sitemaps = {
    'common': CommonStaticViewSitemap,
    'male_static': MaleStaticViewSitemap,
    'male_service_category': MaleServiceCategorySitemap,
    'male_services': MaleServiceSitemap,
    'male_blogs': MaleBlogSitemap,
    'female_static': FemaleStaticViewSitemap,
    'female_service_category': FemaleServiceCategorySitemap,
    'female_services': FemaleServiceSitemap,
    'female_blogs': FemaleBlogSitemap,
}

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', namespace='jet-dashboard')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('rosetta/', include('rosetta.urls')),
    path(settings.ADMIN_URL, admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path('', include('common.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    path('', GenderSelectionPage.as_view(), name='gender_selection'),
    path(_('male/'), include('male.urls', namespace="male")),
    path(_('female/'), include('female.urls', namespace="female")),
)
