from django.urls import path
from django.utils.translation import ugettext_lazy as _
from female import views

app_name = 'female'

urlpatterns = [
    path('', views.FemaleHomePage.as_view(), name="home"),
    path(_('about/'), views.FemaleAboutPage.as_view(), name="about"),
    path(_('services/'), views.FemaleServicesListView.as_view(), name="services"),
    path(_('services/<slug>/'), views.FemaleServicesDetailView.as_view(), name="services_detail"),
    path(_('howitworks/'), views.FemaleHowitworksPage.as_view(), name="howitworks"),
    path(_('before-after/'), views.FemaleBeforeAfterListView.as_view(), name="before_after"),
    path(_('blog/'), views.FemaleBlogListView.as_view(), name="blog_list"),
    path(_('blog/<slug>/'), views.FemaleBlogDetailView.as_view(), name="blog_detail"),
]
