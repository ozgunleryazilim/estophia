from django.urls import path
from django.utils.translation import ugettext_lazy as _
from male import views

app_name = 'male'

urlpatterns = [
    path('', views.MaleHomePage.as_view(), name="home"),
    path(_('about/'), views.MaleAboutPage.as_view(), name="about"),
    path(_('service-categories/'), views.MaleServiceCategoryListView.as_view(), name="service_categories"),
    path(_('service-categories/<slug>/'), views.MaleServiceCategoryDetailView.as_view(),
         name="service_category_detail"),
    path(_('services/'), views.MaleServicesListView.as_view(), name="services"),
    path(_('services/<slug>/'), views.MaleServicesDetailView.as_view(), name="services_detail"),
    path(_('howitworks/'), views.MaleHowitworksPage.as_view(), name="howitworks"),
    path(_('before-after/'), views.MaleBeforeAfterListView.as_view(), name="before_after"),
    path(_('blog/'), views.MaleBlogListView.as_view(), name="blog_list"),
    path(_('blog/<slug>/'), views.MaleBlogDetailView.as_view(), name="blog_detail"),
    path(_('contact/'), views.MaleContactPage.as_view(), name="contact"),
    path(_('gdpr/'), views.MaleKVKKPage.as_view(), name="kvkk"),
]
