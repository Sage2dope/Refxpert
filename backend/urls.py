
from django.contrib import admin
from django.urls import path, include
from refxpert.sitemaps import PostSitemap, StaticViewSitemap
from django.contrib.sitemaps.views import sitemap


sitemaps = {
    'post': PostSitemap,
    'static': StaticViewSitemap,
}

urlpatterns = [
    path("kareem/", admin.site.urls),
    path('sitemap.xml', sitemap,{'sitemaps': sitemaps}),
    path("__reload__/", include("django_browser_reload.urls")),
    path("", include("refxpert.urls")),
]