from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin
from wagtail.models import Page

from .blog_page import BlogPage


class BlogIndexPage(RoutablePageMixin, Page):
    template = "core/blog/blog_index_page.html"
    max_count = 1

    intro_text = models.TextField()

    content_panels = Page.content_panels + [
        FieldPanel("intro_text"),
    ]

    subpage_types = ["core.BlogPage"]

    def get_blog_posts(self) -> list[BlogPage]:
        return BlogPage.objects.live().descendant_of(self).order_by("-first_published_at")

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context.update(
            {"blog_posts": self.get_blog_posts()},
        )
        return context
