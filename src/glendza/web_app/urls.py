from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.contrib.sitemaps.views import sitemap
from wagtail.documents import urls as wagtaildocs_urls

urlpatterns = [
    path(settings.DJANGO_ADMIN_URL, admin.site.urls),
    path(settings.WAGTAIL_ADMIN_URL, include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    re_path(r"^sitemap.xml$", sitemap),
]


if settings.DEBUG:
    from debug_toolbar.toolbar import debug_toolbar_urls
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += debug_toolbar_urls()

# Wagtail URLs (must be added last):
urlpatterns += [
    re_path("", include(wagtail_urls)),
]
